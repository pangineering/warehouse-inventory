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

STATUS_CHOICES = (
    ('In Stock', 'In Stock'),
    ('Need Refill', 'Need Refill'),
     ('Out of Stock', 'Out of Stock'),
     ('Pending','Pending')
)
class Inventory(models.Model):
    number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGOY_CHOICES, max_length=200)
    qty = models.CharField(max_length=200, null=True)
    type = models.CharField(choices=TYPES_CHOICES, max_length=200)
    status = models.CharField(choices=STATUS_CHOICES, max_length=200)
    def __str__(self):
        return  self.name