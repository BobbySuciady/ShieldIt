# Generated by Django 5.0.4 on 2024-04-04 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managerkit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
