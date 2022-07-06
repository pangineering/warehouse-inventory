from django.db import models


class Customers(models.Model):
    number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    status = models.CharField(max_length=200, null=True)  

    def __str__(self):
        return  self.name + ' ' + self.company_name