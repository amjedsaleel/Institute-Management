from django.urls import path
from django.contrib.auth.decorators import login_required

# Local Django
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.InstituteRegistrationView.as_view(), name='register-institute'),
    path('login', views.LoginView.as_view(), name='login'),
]
