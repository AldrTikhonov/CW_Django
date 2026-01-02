from django.urls import path

from mailing import views
from mailing.apps import MailingConfig
from .service import send_mail

from .views import (AttemptListView, ClientCreateView, ClientDeleteView,
                    ClientDetailView, ClientListView, ClientUpdateView,
                    MailingCreateView, MailingDeleteView, MailingDetailView,
                    MailingListView, MailingUpdateView, MessageCreateView,
                    MessageDeleteView, MessageDetailView, MessageListView,
                    MessageUpdateView)

app_name = MailingConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("mailing/", MailingListView.as_view(), name="mailing_list"),
    path("mailing_create/", MailingCreateView.as_view(), name="mailing_create"),
    path(
        "mailing_detail/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"
    ),
    path(
        "mailing_update/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"
    ),
    path(
        "mailing_delete/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete"
    ),
    path("client/", ClientListView.as_view(), name="client_list"),
    path("client_create/", ClientCreateView.as_view(), name="client_create"),
    path("client_detail/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client_update/<int:pk>/", ClientUpdateView.as_view(), name="client_update"),
    path("client_delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),
    path("message/", MessageListView.as_view(), name="message_list"),
    path("message_create", MessageCreateView.as_view(), name="message_create"),
    path(
        "message_detail/<int:pk>/", MessageDetailView.as_view(), name="message_detail"
    ),
    path(
        "message_update/<int:pk>/", MessageUpdateView.as_view(), name="message_update"
    ),
    path(
        "message_delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"
    ),
    path("attempt/", AttemptListView.as_view(), name="attempt_list"),
    path("launch/<int:pk>/", send_mail, name="launch")
]
