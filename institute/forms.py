# Django
from django import forms

# Local Django
from . import models
from .models import Institute, Department, Course


class InstituteForm(forms.ModelForm):
    class Meta:
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Full name of the Institute'}),
            'short_name': forms.TextInput(
                attrs={'placeholder': 'Short Name'}),
            'website': forms.TextInput(
                attrs={'placeholder': 'If you have institute website, please enter website address'}),
            'phone_no': forms.TextInput(attrs={'placeholder': 'Phone no with STD code'}),
        }
        model = Institute
        fields = ['name', 'short_name', 'website', 'phone_no']


class AddDepartmentForm(forms.ModelForm):
    class Meta:
        widgets = {
            'department_name': forms.TextInput(
                attrs={'placeholder': 'Department Name', 'class': 'mt-2'}),
        }

        model = Department
        fields = ['department_name']


class AddCourseForm(forms.ModelForm):
    # p = forms.ModelChoiceField(Department.objects.all())

    class Meta:
        widgets = {
            'course': forms.TextInput(
                attrs={'placeholder': 'Course Name', 'class': 'mt-2'}),
        }

        model = Course
        fields = ['institute', 'department', 'course']

    def __init__(self, *args, **kwargs):
        institute = kwargs.pop('institute', None)
        super(AddCourseForm, self).__init__(*args, **kwargs)

        if institute:
            self.fields['department'].queryset = Department.objects.filter(institute=institute)
