from django.db import models

from companies.models import Company


class Vehicle(models.Model):

    FUEL_TYPES = (
        ('d', 'Diesel'),
        ('g', 'Gasoline')
    )

    license_plate = models.CharField(max_length=15)
    manufacturer = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    purchase_date = models.DateField()
    warranty_end_date = models.DateField()
    company_owner = models.ForeignKey(Company, on_delete=models.DO_NOTHING, blank=False, null=True)
    fuel_type = models.CharField(max_length=1, choices=FUEL_TYPES)
    is_active = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('add', 'Add'),
            ('edit', 'Edit'),
            ('delete', 'Delete'),
        )

    def __str__(self):
        return self.license_plate

    def getFTypeName(self):
        companyName = 'Дизел' if self.fuel_type == 'd' else 'Бензин'
        return companyName

    def getIsActive(self):
        isActive = 'Да' if self.is_active is True else 'Не'
        return isActive


