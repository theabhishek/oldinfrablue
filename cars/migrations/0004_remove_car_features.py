# Generated by Django 4.0.1 on 2023-01-21 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
    ]
