# Generated by Django 2.2.dev20180816134906 on 2018-08-28 11:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20180828_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(max_length=15, validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]
