from django.core.validators import MinValueValidator
from django.db import models

from companies.models import Company


class JobPosition(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=25)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

class Employee(models.Model):

    SEX_TYPES = (
        ('m', 'Male'),
        ('f', 'Female')
    )


    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    egn = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=55, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, blank=False, null=True)
    job_position = models.ForeignKey('JobPosition', on_delete=models.DO_NOTHING, blank=False, null=True)
    salary = models.FloatField()
    date_of_appointment = models.DateField()
    date_of_dismiss = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('add', 'Add'),
            ('edit', 'Edit'),
            ('delete', 'Delete'),
        )

    def __str__(self):
        return self.first_name + ' ' + self.second_name + ' ' + self.last_name

    def getSexType(self):
        type = 'Мъж' if self.sex == 'm' else 'Жена'
        return type

    def getDateData(self):
        date = '' if self.date_of_dismiss is None else self.date_of_dismiss
        return date

    def getIsActiveEmp(self):
        isActive = 'Да' if self.is_active is True else 'Не'
        return isActive