# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import user

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ['username', 'email', 'password', 'gender']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
