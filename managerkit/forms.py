# user_management/forms.py
from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'sex', 'dietary_restrictions', 'age']
