# Generated by Django 4.0.6 on 2023-02-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]