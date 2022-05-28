from django.db import models

# Create your models here.
CATEGOY_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)

TYPES_CHOICES = (
    ('Buy', 'Buy'),
    ('Sell', 'Sell')
)
class Inventory(models.Model):
    number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGOY_CHOICES, max_length=200)
    qty = models.CharField(max_length=200, null=True)
    type = models.CharField(choices=TYPES_CHOICES, max_length=200)
    status = models.CharField(max_length=200, null=True)  
    def __str__(self):
        return  self.name