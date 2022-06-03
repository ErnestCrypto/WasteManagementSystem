# Creating our models of the Admins
from django.db import models
from Basemodel.models import DAYS


class Administrators(models.Model):
    username = models.CharField(max_length=255, default=None, null=True)
    profile = models.ImageField(upload_to='images/', default=None, null=True)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=255, default=None)
    contact = models.TextField(default=None)

    class Meta:
        verbose_name_plural = ('Administrators')

    def __str__(self):
        return self.username


class Drivers(models.Model):
    firstname = models.CharField(max_length=255, default=None, null=True)
    lastname = models.CharField(max_length=255, default=None)
    profile = models.ImageField(upload_to='images/', default=None)
    email = models.EmailField(default=None)
    contact = models.IntegerField(default=None)
    day = models.IntegerField(choices=DAYS, default=None)
    location = models.CharField(max_length=255, default=None)
    truck_id = models.CharField(max_length=255, default=None)

    class Meta:
        verbose_name_plural = ('Drivers')


class Trucks(models.Model):
    driver_id = models.CharField(max_length=255, default=None, null=True)
    number_plate = models.CharField(max_length=255, default=None)
    details = models.TextField(default=None)

    class Meta:
        verbose_name_plural = ('Trucks')
