from django.db import models

class App(models.Model):

    name = models.CharField(max_length=25)
    url = models.CharField(max_length=25)
    model_class = models.CharField(max_length=10)
    code = models.CharField(max_length=25, blank=True)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
