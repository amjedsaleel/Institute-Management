# Django
from django.urls import path

# Local Django
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.index, name='index')
]