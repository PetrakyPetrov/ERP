# Generated by Django 2.2.dev20180816134906 on 2018-08-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fms', '0005_auto_20180828_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=15),
        ),
    ]
