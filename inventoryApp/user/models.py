from email.policy import default
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
TEAM_CHOICES = (
    ('Robotics', 'Robotics'),
    ('Automobile', 'Automobile'),
    ('Machine', 'Machine'),
)
CATEGOY_CHOICES = (
    ('Manager', 'Manager'),
    ('Sales', 'Sales'),
    ('Engineer', 'Engineer'),
    ('Warehouse', 'Warehouse'),
)


# class Profile(models.Model): 
#     id = models.CharField(max_length=200,primary_key=True) #(User, on_delete=models.CASCADE,default=99)
#     employee_number = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     team = models.CharField(choices=TEAM_CHOICES, max_length=200)
#     position = models.CharField(choices=CATEGOY_CHOICES, max_length=200)

#     def __str__(self):
#         return  self.employee_number + "_" + self.position

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,related_name="user_profile")
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_number = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    team = models.CharField(choices=TEAM_CHOICES, max_length=200)
    position = models.CharField(choices=CATEGOY_CHOICES, max_length=200)

    def __str__(self):
        return  self.employee_number + "_" + self.position + '_' + str(self.user)