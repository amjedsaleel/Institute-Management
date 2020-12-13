from django.urls import path

# Local Django
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.InstituteRegistrationView.as_view(), name='register-institute'),
]