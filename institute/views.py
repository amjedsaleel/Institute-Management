# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# LocalDjango
from .forms import AddDepartmentForm, AddCourseForm
from .models import Institute, Department


# Create your views here.


class IndexView(LoginRequiredMixin, View):
    """
    This view for render dashboard for the institute.
    And pass data to dashboard page with all details about the institute.
    It passes student, teachers, department and course details.
    """

    def get(self, request, institute_short_name):
        context = {
            'institute_short_name': institute_short_name
        }
        return render(request, 'institute/dashboard.html', context)

    def post(self, request):
        pass


class AdministrationView(LoginRequiredMixin, View):

    def get(self, request, institute_short_name):

        institute = request.user.institute

        department_form = AddDepartmentForm()
        course_form = AddCourseForm(institute=institute)

        context = {
            'institute_short_name': institute_short_name,
            'department_form': department_form,
            'course_form': course_form
        }

        return render(request, 'institute/administration.html', context)


class AddDepartment(LoginRequiredMixin, View):
    """
    This view for adding department in the institute
    """

    def get(self, request, institute_short_name):
        """
        the get function just returns the form for adding department
        """
        form = AddDepartmentForm()

        context = {
            'institute_short_name': institute_short_name,
            'form': form
        }
        return render(request, 'institute/add_department.html', context)

    def post(self, request, institute_short_name):
        """
        when post request come from client side for department,
        the function post will executed
        """
        institute_name = request.user.institute
        form = AddDepartmentForm(request.POST)

        if form.is_valid():  # Checking the form is valid or not
            print('valid')
            department_name = form.cleaned_data['department_name']

            # try/catch
            try:
                """
                the both field institute and institute must unique_together.
                if institute and institute not added before with same department name,
                Then execute try block otherwise execute catch block.
                """
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


class AddCourse(View):
    """
    This view for adding course in the institute
    """

    def get(self, request, institute_short_name):
        """
       the get function just returns the form for adding course
       """
        institute = request.user.institute
        form = AddCourseForm(institute=institute)

        context = {
            'institute_short_name': institute_short_name,
            'form': form,
        }
        return render(request, 'institute/add_course.html', context)

    def post(self, request, institute_short_name):
        """
        when post request come from client side for adding course,
        the function post will executed
       """
        institute = request.user.institute
        form = AddCourseForm(request.POST, institute=institute)

        if form.is_valid():
            course = form.cleaned_data['course']

            try:
                """
                the both field department and course must unique_together.
                if department and course not added before with same values,
                Then execute try block otherwise execute catch block.
               """
                object = form.save(commit=False)
                object.institute = institute
                object.save()
                messages.success(request, f'{course} course is successfully added')
                return redirect('institute:add-course', institute_short_name=institute_short_name)
            except:
                messages.error(request, f'{course} course with this Institute is  already exists.')

            return redirect('institute:add-course', institute_short_name=institute_short_name)

        context = {
            'institute_short_name': institute_short_name,
            'form': form,
        }

        return render(request, 'institute/add_course.html', context)
