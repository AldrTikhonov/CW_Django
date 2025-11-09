from django.shortcuts import render
from mailing.models import Mailing, Client, Message

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ClientListView(ListView):
    """
    Класс, представляющий отображение списка клиентов.
    """
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "client"


class ClientCreateView(CreateView):
    """
    Класс, представляющий нового клиента.
    """
    model = Client
    template_name = "client/client_form.html"
    success_url = reverse_lazy("mailing:client_list")


class ClientUpdateView(UpdateView):
    """
    Класс, представляющий обновление клиента.
    """
    model = Client
    template_name = "client/client_form.html"
    success_url = reverse_lazy = ("mailing:client_list")


class ClientDetailView(DetailView):
    """
    Класс, представляющий детальное отображение клиента.
    """
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client"


class ClientDeleteView(DeleteView):
    """
    Класс, представляющий удаление клиента.
    """
    model = Client
    template_name = "client/client_confirm_delete.html"
    success_url = reverse_lazy("mailing:client_list")


class MessageListView(ListView):
    """
    Класс, представляющий отображение списка клиентов.
    """
    model = Message
    template_name = "message/message_list.html"
    context_object_name = "message"


class MessageCreateView(CreateView):
    """
    Класс, представляющий нового клиента.
    """
    model = Message
    template_name = "message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageUpdateView(UpdateView):
    """
    Класс, представляющий обновление клиента.
    """
    model = Message
    template_name = "message/message_form.html"
    success_url = reverse_lazy("mailing:message_list")


class MessageDetailView(DetailView):
    """
    Класс, представляющий детальное отображение клиента.
    """
    model = Message
    template_name = "message/message_detail.html"
    context_object_name = "message"


class MessageDeleteView(DeleteView):
    """
    Класс, представляющий удаление клиента.
    """
    model = Message
    template_name = "message/message_confirm_delete.html"
    success_url = reverse_lazy("mailing:message_list")


class MailingListView(ListView):
    """
    Класс, представляющий отображения списка рассылок.
    """
    model = Mailing
    template_name = "mailing/mailing_list.html"
    context_object_name = "mailing"


class MailingCreateView(CreateView):
    """
    Класс, представляющий создание новой рассылки.
    """
    model = Mailing
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
    template_name = "mailing/mailing_form.html"
    success_url = reverse_lazy("mailing:mailing_list")


class MailingDeleteView(DeleteView):
    """
    Класс, представляющий удаление рассылки.
    """
    model = Mailing
    template_name = "mailing/mailing_confirm_delete.html"
    success_url = reverse_lazy("mailing:mailing_list")




def home(request):
    mailings = Mailing.objects.all()
    context = {"mailing": mailings}
    return render(request, 'mailing/home.html', context)




