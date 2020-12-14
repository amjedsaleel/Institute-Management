# Django
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import View

# Create your views here.


class InstituteRegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register-institute.html',)

    def post(self, request):
        return render(request, 'accounts/register-institute.html', )
