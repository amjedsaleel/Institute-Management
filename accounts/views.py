# Django
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import auth

# Local Django
from . forms import CustomUserCreationForm, LoginForm
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
            # user.role = 'institute'
            user.is_institute = True
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


class LoginView(View):
    def get(self, request):
        form = LoginForm()

        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                if user.is_student:
                    pass

                if user.is_teacher:
                    pass

                if user.is_institute:
                    return redirect('institute:index', institute_short_name=user.institute.short_name)

            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('accounts:login')

        return render(request, 'accounts/login.html', {'form': form})


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        print('logout')
        messages.success(request, 'You have been logged out')
        return redirect('accounts:login')
