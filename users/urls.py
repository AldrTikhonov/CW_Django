from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import CustomUserCreateView, email_verification

app_name = UsersConfig

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view(template_name='logout.html')),
    path('register/', CustomUserCreateView.as_view(template_name='register')),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm')
]