# Django
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm:', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }

        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password:', max_length=100,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
