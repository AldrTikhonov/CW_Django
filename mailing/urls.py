from django.urls import path

from mailing import views
from mailing.apps import MailingConfig
from .views import MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),

    path("mailing/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/new/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing/update/<int:pk>/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing/delete/<int:pk>/", MailingDeleteView.as_view(), name="mailing_delete")
]