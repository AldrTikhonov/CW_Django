from django.shortcuts import render
from mailing.models import Mailing, Client, Message, MailingAttempt
from mailing.forms import MailingForm, ClientForm, MessageForm, MailingAttemptForm

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ClientListView(ListView):
    """
    Класс, представляющий отображение списка клиентов.
    """
    model = Client
    template_name = "mailing/client_list.html"
    context_object_name = "client"


class ClientCreateView(CreateView):
    """
    Класс, представляющий нового клиента.
    """
    model = Client
    form_class = ClientForm
    template_name = "mailing/client_form.html"
    success_url = reverse_lazy("mailing:client_list")


class ClientUpdateView(UpdateView):
    """
    Класс, представляющий обновление клиента.
    """
    model = Client
    form_class = ClientForm
    template_name = "mailing/client_form.html"
    success_url = reverse_lazy("mailing:client_list")


class ClientDetailView(DetailView):
    """
    Класс, представляющий детальное отображение клиента.
    """
    model = Client
    template_name = "mailing/client_detail.html"
    context_object_name = "client"


class ClientDeleteView(DeleteView):
    """
    Класс, представляющий удаление клиента.
    """
    model = Client
    template_name = "mailing/client_confirm_delete.html"
    success_url = reverse_lazy("mailing:client_list")


class MessageListView(ListView):
    """
    Класс, представляющий отображение списка сообщений.
    """
    model = Message
    template_name = "mailing/message_list.html"
    context_object_name = "message"


class MessageCreateView(CreateView):
    """
    Класс, представляющий нового сообщения.
    """
    model = Message
    form_class = MessageForm
    template_name = "mailing/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageUpdateView(UpdateView):
    """
    Класс, представляющий обновление сообщения.
    """
    model = Message
    form_class = MessageForm
    template_name = "mailing/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDetailView(DetailView):
    """
    Класс, представляющий детальное отображение сообщения.
    """
    model = Message
    template_name = "mailing/message_detail.html"
    context_object_name = "message"


class MessageDeleteView(DeleteView):
    """
    Класс, представляющий удаление сообщения.
    """
    model = Message
    template_name = "mailing/message_confirm_delete.html"
    success_url = reverse_lazy("mailing:message_list")


class MailingListView(ListView):
    """
    Класс, представляющий отображения списка рассылок.
    """
    model = Mailing
    template_name = "mailing/mailing_list_1.html"
    context_object_name = "mailing"


class MailingCreateView(CreateView):
    """
    Класс, представляющий создание новой рассылки.
    """
    model = Mailing
    form_class = MailingForm
    template_name = "mailing/mailing_form.html"
    success_url = reverse_lazy("mailing:mailing_list")


class MailingDetailView(DetailView):
    """
    Класс, представляющий детали определенной рассылки.
    """
    model = Mailing
    template_name = "mailing/mailing_detail.html"
    context_object_name = "mailing"


class MailingUpdateView(UpdateView):
    """
    Класс, представляющий обновление рассылки.
    """
    model = Mailing
    form_class = MailingForm
    template_name = "mailing/mailing_form.html"
    success_url = reverse_lazy("mailing:mailing_list")


class MailingDeleteView(DeleteView):
    """
    Класс, представляющий удаление рассылки.
    """
    model = Mailing
    template_name = "mailing/mailing_confirm_delete.html"
    success_url = reverse_lazy("mailing:mailing_list")

    def test_func(self):
        mailing = self.get_object()
        user = self.request.user
        return mailing.owner_id == user.id


class MailingAttemptListView(ListView):
    """
    Класс, представляющий отображение списка попыток.
    """
    model = MailingAttempt
    template_name = "mailing/attempt_list.html"
    context_object_name = "attempt"


class MailingAttemptCreateView(CreateView):
    """
    Класс, представляющий отображение новой попытки.
    """
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = "mailing/attempt_form.html"
    success_url = reverse_lazy("mailing:attempt_list")


class MailingAttemptUpdateView(UpdateView):
    """
    Класс, представляющий обновление попытки.
    """
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = "mailing/attempt_form.html"
    success_url = reverse_lazy("mailing:attempt_list")


class MailingAttemptDetailView(DetailView):
    """
    Класс, представляющий детальное отображение попытки.
    """
    model = MailingAttempt
    template_name = "mailing/attempt_detail.html"
    context_object_name = "attempt"


class MailingAttemptDeleteView(DeleteView):
    """
    Класс, представляющий удаление попытки.
    """
    model = MailingAttempt
    template_name = "mailing/attempt_confirm_delete.html"
    success_url = reverse_lazy("mailing:attempt_list")


def home(request):
    mailings = Mailing.objects.all()
    context = {"mailing": mailings}
    return render(request, 'mailing/home.html', context)
