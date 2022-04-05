# Creating our models from the Users
from django.db import models
from Admin.models import Requests, HelpCenter


class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    pricing = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    balance = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='images/')
    contact = models.IntegerField()

    class Meta:
        verbose_name_plural = ('Users')


class Payments(models.Model):
    user_id = models.IntegerField()
    mode = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    amount = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ('Payments')
