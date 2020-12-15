from django.urls import path
from django.contrib.auth.decorators import login_required

# Local Django
from . import views

app_name = 'student'

urlpatterns = [
    path('',  login_required(views.IndexView.as_view()), name='index'),
]
