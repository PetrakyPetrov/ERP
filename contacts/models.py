from django.db import models

class Contact(models.Model):

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=55, blank=True, null=True)
    is_company = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('add', 'Add'),
            ('edit', 'Edit'),
            ('delete', 'Delete'),
        )

    def __str__(self):
        return self.name

    def getIsCompany(self):
        isCompany = 'Да' if self.is_company is True else 'Не'
        return isCompany

    # def createContact(self, title):
    #     book = self.create(title=title)
    #     return book
