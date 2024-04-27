# forms.py

from django import forms
# from django.contrib.auth.models import User
from .models import user

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ['username', 'email', 'password', 'gender']
