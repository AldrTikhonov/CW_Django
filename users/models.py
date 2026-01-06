from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name="Телефон",
        help_text="Укажите номер телефона"
    )
    country = models.CharField(
        max_length=150, **NULLABLE, verbose_name="Страна", help_text="Укажите страну"
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар"
    )

    token = models.CharField(max_length=100, **NULLABLE, verbose_name="Токен")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        ["username"]
    )  # для создания суперпользователя(superuser) в терминале PyCharm, нужно в данной строке задать значение "username" и в терминале запустить команду python3 manage.py createsuperuser, далее заполнять данные.

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
