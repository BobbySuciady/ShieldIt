"""
CHANGES TO THIS FILE? DO:
- python manage.py makemigrations
- python manage.py migrate
"""

from django import forms
from .models import User, Item, Category

# forms.py is to function to put things in the database

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'sex', 'dietary_restrictions', 'age']

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'description']


