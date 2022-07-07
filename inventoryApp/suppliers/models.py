from django.db import models


class Suppliers(models.Model):
    number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    def __str__(self):
        return  self.name + ' ' + self.company_name