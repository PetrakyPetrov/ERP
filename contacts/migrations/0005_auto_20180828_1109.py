# Generated by Django 2.2.dev20180816134906 on 2018-08-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20180828_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
