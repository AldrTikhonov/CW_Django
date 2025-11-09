from django.db import models

NULLABLE = {"blank": True, "null": True}




class Client(models.Model):
    """
    Модель, представляющая клиента сервиса отправки рассылок.
    """
    email = models.EmailField(verbose_name="Почта", help_text="Укажите почту")
    full_name = models.CharField(max_length=240, verbose_name="ФИО", help_text="Укажите ФИО")
    comment = models.TextField(verbose_name="Комментарий", **NULLABLE, help_text="Напишите комментарий")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.email


class Message(models.Model):
    """
    Модель, представляющая сообщение рассылки.
    """
    subject = models.CharField(max_length=200, verbose_name="тема сообщения", help_text="Укажите тему сообщения")
    body = models.TextField(verbose_name="сообщение", help_text="Напишите сообщение")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    """
    Модель, представляющая рассылку.
    """
    CREATED = "CREATED"
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    STATUS_CHOICES = [
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
        (COMPLETED, "Завершена"),
    ]
    start_datetime = models.DateTimeField(verbose_name="Дата и время отправки")
    end_datetime = models.DateTimeField(verbose_name="Дата и время завершения рассылки", **NULLABLE)
    status = models.CharField(max_length=25, verbose_name="Статус", choices=STATUS_CHOICES, default=CREATED)
    message = models.ForeignKey(Message, verbose_name="Сообщение", on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f"{self.message} - {self.start_datetime}"


class MailingAttempt(models.Model):
    """
    Модель, представляющая попытку отправки рассылки.
    """
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    STATUS_CHOICE = [
        (SUCCESS, "Удачная"),
        (FAILED, "Неудачная"),
    ]
    mailing = models.ForeignKey(Mailing, verbose_name="Рассылка", on_delete=models.CASCADE, related_name="attempts")
    attempt_datetime = models.DateTimeField(verbose_name="Дата и время попытки отправки", auto_now_add=True)
    status = models.CharField(max_length=25, verbose_name="Статус", choices=STATUS_CHOICE)
    server_response = models.TextField(verbose_name="Ответ сервера", **NULLABLE)

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"

    def __str__(self):
        return f"{self.mailing} - {self.attempt_datetime}"