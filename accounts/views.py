# Django
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

# Local Django
from .models import User
from institute.models import Institute

# Create your views here.


class InstituteRegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register-institute.html', )

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        institute = request.POST['institute']
        short_name = request.POST['short-name']

        # try/catch
        try:
            website = request.POST['website']
        except:
            website = None

        # try/catch
        try:
            phone = request.POST['phone']
        except:
            phone = None

        if password1 != password2:
            messages.warning(request, 'Password not matching')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken, please choose another')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken, please choose another')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password1,
                        role='institute'
                    )
                    user.save()

                    institute = Institute.objects.create(
                        user=user,
                        name=institute,
                        short_name=short_name,
                        website=website,
                        phone_no=phone
                    )
                    institute.save()

                    messages.success(request, 'Account is Successfully Created')
                    return redirect('about:index')
        return render(request, 'accounts/register-institute.html',)
