from django.contrib.auth.forms import UserCreationForm

from mailing.forms import StyleFormMixin
from .models import CustomUser


class CustomUserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

