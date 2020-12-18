# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# LocalDjango
from .forms import AddDepartmentForm
from .models import Institute
from accounts.models import User


# Create your views here.


class IndexView(LoginRequiredMixin, View):
    def get(self, request, institute_short_name):
        context = {
            'institute_short_name': institute_short_name
        }
        return render(request, 'institute/dashboard.html', context)

    def post(self, request):
        pass


class AddDepartment(LoginRequiredMixin, View):
    def get(self, request, institute_short_name):
        form = AddDepartmentForm()

        context = {
            'institute_short_name': institute_short_name,
            'form': form
        }
        return render(request, 'institute/add_department.html', context)

    def post(self, request, institute_short_name):
        institute_name = request.user.institute
        form = AddDepartmentForm(request.POST)

        if form.is_valid():
            print('valid')
            department_name = form.cleaned_data['department_name']

            try:
                object = form.save(commit=False)
                object.institute = institute_name
                object.save()
                messages.success(request, f'{department_name} department is successfully added')
            except:
                messages.error(request, f'{department_name} Department with this Institute is  already exists.')

            return redirect('institute:add-department', institute_short_name=institute_short_name)

        context = {
            'institute_short_name': institute_short_name,
            'form': form
        }

        return render(request, 'institute/add_department.html', context)
