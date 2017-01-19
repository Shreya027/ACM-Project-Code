

from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(null=True,blank=True)
    location = models.CharField(max_length=300)
    notes = models.CharField(max_length=800)
    def __str__(self):
        return self.name

class List(models.Model):
    destination=models.CharField(max_length=200)
    def __str__(self):
        return self.destination

class Country(models.Model):
    name = models.CharField(max_length=80)
    image = models.FileField(null=True,blank=True)
    description = models.CharField(max_length=800)
    capital = models.CharField(max_length=30)
    def __str__(self):
        return self.name





