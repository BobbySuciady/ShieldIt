# Generated by Django 5.0.4 on 2024-04-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("managerkit", "0007_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
