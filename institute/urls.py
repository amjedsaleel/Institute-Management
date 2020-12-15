from django.urls import path

# Local Django
from . import views

app_name = 'institute'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index',)
]
