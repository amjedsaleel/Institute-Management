# Django
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

# Local Django
from .models import User
from . forms import CustomUserCreationForm
from institute.forms import InstituteForm

# Create your views here.


class InstituteRegistrationView(View):
    def get(self, request):
        institute_form = InstituteForm()
        user_register_form = CustomUserCreationForm()

        context = {
            'institute_form': institute_form,
            'user_register_form': user_register_form
        }

        return render(request, 'accounts/register-institute.html', context)

    def post(self, request):
        user_register_form = CustomUserCreationForm(request.POST)
        institute_form = InstituteForm(request.POST)

        print(institute_form.is_valid())

        if (user_register_form.is_valid()) and (institute_form.is_valid()):
            user = user_register_form.save(commit=False)
            user.role = 'institute'
            user.save()

            institute = institute_form.save(commit=False)
            institute.user = user
            institute.save()
            messages.success(request, 'Successfully Account created')
            return redirect('about:index')

        context = {
            'institute_form': institute_form,
            'user_register_form': user_register_form
        }

        return render(request, 'accounts/register-institute.html', context)



