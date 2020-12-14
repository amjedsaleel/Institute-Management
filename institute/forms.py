# Django
from django import forms

# Local Django
from .models import Institute


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