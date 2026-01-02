import smtplib
from datetime import datetime

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from config import settings
from mailing.models import Mailing, MailingAttempt
import pytz


def send_mail(request, pk):
    """Функция отправки запуска рассылки в любое время вне расписания.
    Отправляет письма, записывает логи с информацией об отпрвке
    Также записывает логи об ошибках в случае их возникновения."""

    t_zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(t_zone)
    mailing_data = get_object_or_404(Mailing, pk=pk)

    if mailing_data.is_active:

        change_mailing_status(mailing_data, current_datetime)

        emails = [recipient.email for recipient in mailing_data.clients.all()]

        try:
            server_response = send_mail(subject=mailing_data.message.subject, message=mailing_data.message.body,
                                        from_email=settings.EMAIL_HOST_USER, recipient_list=emails,
                                        fail_silently=False)
            print("Письмо отправлено")
            status = "Отправлено"
            mailing_attempt = MailingAttempt(mailing=mailing_data, status=status,
                                              server_response=server_response, owner=mailing_data.owner)
            mailing_attempt.save()
            print("попытка рассылки сохранена")

        except smtplib.SMTPException as error:
            status = "Не отправлено"
            server_response = f"Ошибка отправки {error}"
            mailing_attempt = MailingAttempt(mailing=mailing_data, status=status,
                                              server_response=server_response, owner=mailing_data.owner)
            mailing_attempt.save()
            print("ошибка попытка рассылки:", error)

        finally:
            return redirect(reverse("mailing:mailing_list"))

    else:
        print("Рассылка не активна")
        return redirect(reverse("mailing:mailing_list"))
