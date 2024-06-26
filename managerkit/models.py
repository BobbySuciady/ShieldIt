"""
CHANGES TO THIS FILE? DO:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
"""
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

# models.py is to make databse tables
# Make all null = False later
class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'N'
    TRANS = 'T'
    OTHER = 'O'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Non-binary'),
        (TRANS, 'Trans'),
        (OTHER, 'Other'),
    ]

    RELATIONSHIP_CHOICES = [
        ('Primary User', 'Primary User'),
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Husband', 'Husband'),
        ('Wife', 'Wife'),
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Cousin (male)', 'Cousin (male)'),
        ('Cousin (female)', 'Cousin (female)'),
        ('Nephew', 'Nephew'),
        ('Niece', 'Niece'),
        ('Grandfather', 'Grandfather'),
        ('Grandmother', 'Grandmother'),
        ('Grandson', 'Grandson'),
        ('Granddaughter', 'Granddaugher'),
        ('Other', 'Other'),
    ]
    DIETARY_RESTRICTION_CHOICES = [
        ('No Dietary Restrictions', 'No Restrictions'),
        ('FODMAP', 'FODMAP'),
        ('Gluten Free', 'Gluten Free'),
        ('Lactose Free', 'Lactose Free'),
        ('Nut Free', 'Nut Free'),
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Other', 'Other'),
    ]

    MEDICAL_CONDITIONS_CHOICES = [
        ('No Medical Conditions', 'No Conditions'),
        ('Asthma', 'Asthma'),
        ('Diabetes', 'Diabetes'),
        ('Hypertension', 'Hypertension'),
        ('Allergies', 'Allergies'),
        ('Other', 'Other'),
    ]
    
    DISABILITY_CHOICES = [
        ('Disable', 'Disable'),
        ('Non-disable', 'Non-disable'),
    ]
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=False, blank=False)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(99, message=_("Age must be below 100"))], null=False, blank=False)
    relationship = models.TextField(choices=RELATIONSHIP_CHOICES, null=False, blank=False)
    dietary_restrictions = models.TextField(choices=DIETARY_RESTRICTION_CHOICES, null=False, blank=False)
    medical_conditions = models.TextField(choices=MEDICAL_CONDITIONS_CHOICES, null=False, blank=False)
    disability = models.TextField(choices=DISABILITY_CHOICES, null=False, blank=False)

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
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name

# In your models.py or a separate models file
class ExpiringItem(models.Model):
    name = models.CharField(max_length=100)
    expiry_date = models.DateField()

