# user_management/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    dietary_restrictions = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
