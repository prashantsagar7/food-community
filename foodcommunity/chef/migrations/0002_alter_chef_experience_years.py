# Generated by Django 4.2.3 on 2023-08-04 11:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='experience_years',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]