from django.db import models
from django.forms import ImageField

# Create your models here.
CATEGOY_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)

TYPES_CHOICES = (
    ('Standard', 'Standard'),
    ('Custom', 'Custom')
)

STATUS_CHOICES = (
    ('Not Start', 'Not Start'),
    ('In Progress', 'In Progress'),
    ('Change Order', 'Change Order'),
    ('Done', 'Done'),
    ('Deliver', 'Deliver'),
    ('Approve', 'Approve')
)
class Products(models.Model):
    number = models.CharField(max_length=200,unique=True,primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGOY_CHOICES, max_length=200)
    qty = models.IntegerField()
    type = models.CharField(choices=TYPES_CHOICES, max_length=200,null=True)
    #img = models.ImageField(upload_to='products', height_field=None, width_field=None, max_length=100)
    #status = models.CharField(choices=STATUS_CHOICES, max_length=200)
    def __str__(self):
        return  self.name