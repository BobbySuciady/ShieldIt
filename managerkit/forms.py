"""
CHANGES TO THIS FILE? DO:
- python manage.py makemigrations
- python manage.py migrate
"""

from django import forms
from .models import User, Item, Category

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'sex', 'age', 'dietary_restrictions', 'medical_conditions', 'disability']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        
