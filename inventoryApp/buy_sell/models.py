from email.policy import default
from unicodedata import category
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from jsonfield import JSONField


CATEGOY_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)
TEAM_CHOICES = (
    ('Manager', 'Manager'),
    ('Sales', 'Sales'),
    ('Engineer', 'Engineer'),
    ('Warehouse', 'Warehouse'),
)
STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Approve', 'Approve'),
    ('Complete', 'Complete'),
    ('Cancel', 'Cancel'),
    ('Revision', 'Revision'),
)


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    p_num = models.CharField(max_length=200,unique=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200) 
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False)
    team = models.CharField(choices=TEAM_CHOICES, max_length=200)
    status = models.CharField(choices=STATUS_CHOICES, max_length=200)
    category = models.CharField(choices=CATEGOY_CHOICES, max_length=200)
    item = models.CharField(max_length=200, default='')
    qty = models.IntegerField(default=0)

    def __str__(self):
        return  self.employee_number + "_" + self.position + '_' + str(self.user)


class Selling(models.Model):
    id = models.AutoField(primary_key=True)
    s_num = models.CharField(max_length=200,unique=True)
    name = models.CharField(max_length=200)  
    date = models.DateTimeField(auto_now=False)
    team = models.CharField(choices=TEAM_CHOICES, max_length=200)
    status = models.CharField(choices=STATUS_CHOICES, max_length=200)
    category = models.CharField(choices=CATEGOY_CHOICES, max_length=200)
    item = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return  str(self.s_num) + '_' + self.team + "_" + self.category + '_' + self.status + '_' + str(self.date) 