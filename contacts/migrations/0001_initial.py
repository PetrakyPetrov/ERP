# Generated by Django 2.2.dev20180816134906 on 2018-08-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=55)),
                ('is_company', models.BooleanField(default=True)),
            ],
        ),
    ]
