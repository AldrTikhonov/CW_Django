from django.contrib.auth.forms import UserCreationForm

from mailing.forms import StyleFormMixin

from .models import User

# class CustomCreationForm(StyleFormMixin, UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ("email", "password1", "password2")


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
