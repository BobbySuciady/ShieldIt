"""
CHANGES TO THIS FILE? DO:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
"""
from django.db import models

# models.py is to make databse tables
# Make all null = False later
class User(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10) # Should be enum type
    dietary_restrictions = models.CharField(max_length=100)
    age = models.IntegerField() # Restrict up to 100?

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    expiry_date = models.DateField(null=True)
    quantity = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
