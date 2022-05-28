from email.policy import default
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
TYPE_CHOICES = (
    ('Invoice', 'Invoice'),
    ('Change', 'Change'),
    ('Order', 'Order'),
    ('Finance', 'Finance'),
)

LEVEL_CHOICES = (
    ('Major', 'Major'),
    ('Minor', 'Minor'),
)

STATUS_CHOICES = (
    ('Open', 'Open'),
    ('Close', 'Close'),
)

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    subject =  models.CharField(max_length=200)
    date = models.DateTimeField()
    note = models.TextField(blank = True)

    def __str__(self):
        return  str(self.id) + '_' + str(self.date) + '_' + self.subject

class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    tweet_by =  models.CharField(max_length=200)
    note = models.TextField(blank = True)

    def __str__(self):
        return  str(self.id) + '_' + str(self.date) + '_' + self.twwet_by

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    subject =  models.CharField(max_length=200)
    date = models.DateTimeField()
    note = models.TextField(blank = True)

    def __str__(self):
        return  str(self.id) + '_' + str(self.date) + '_' + self.subject

class Memo(models.Model):
    id = models.AutoField(primary_key=True)
    subject =  models.CharField(max_length=200)
    date = models.DateTimeField()
    sender = models.CharField(max_length=200)
    reciever = models.CharField(max_length=200)
    note = models.TextField(blank = True)

    def __str__(self):
        return  str(self.id) + '_' + str(self.date) + '_' + self.subject

class Outstanding(models.Model):
    id = models.AutoField(primary_key=True)
    subject =  models.CharField(max_length=200)
    date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=200)
    type = models.CharField(choices=TYPE_CHOICES, max_length=200)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=200)
    note = models.TextField(blank = True)

    def __str__(self):
        return  str(self.id) + '_' + str(self.date) + '_' + self.subject + '_' + self.type + '_' + self.level + '_' + self.status  