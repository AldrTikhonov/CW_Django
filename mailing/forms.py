from django.forms import BooleanField, ModelForm

from .models import Client, Mailing, MailingAttempt, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"
        exclude = ["owner"]
        # fields = ["status", "message", "clients"]


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ["email", "full_name", "comment"]


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ["subject", "body"]


class MailingAttemptForm(StyleFormMixin, ModelForm):
    class Meta:
        model = MailingAttempt
        fields = ["mailing", "status", "server_response"]
