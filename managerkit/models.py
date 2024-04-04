"""
CHANGES TO THIS FILE? DO:
- python manage.py makemigrations
- python manage.py migrate
"""
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    dietary_restrictions = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

