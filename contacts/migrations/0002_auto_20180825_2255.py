# Generated by Django 2.2.dev20180816134906 on 2018-08-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_company',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
