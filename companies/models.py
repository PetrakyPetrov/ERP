from django.db import models

class Company(models.Model):

    name = models.CharField(max_length=255)
    mrp = models.CharField(max_length=50)
    vat = models.CharField(max_length=50)
    idn = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25)
    parent_company = models.ForeignKey('self', on_delete=models.DO_NOTHING,  blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('add', 'Add'),
            ('edit', 'Edit'),
            ('delete', 'Delete'),
        )

    def __str__(self):
        return self.name

    def getPCompanyName(self):
        companyName = '----' if self.parent_company is None else self.parent_company.name
        return companyName

    def getIsActive(self):
        isActive = 'Да' if self.is_active is True else 'Не'
        return isActive

