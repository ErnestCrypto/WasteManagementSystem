# Creating our models from the Login
from django.db import models
from Basemodel.models import TYPE, DAYS


class Login(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    pricing = models.CharField(max_length=255)
    day = models.IntegerField(choices=DAYS, default=None)
    balance = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='images/')
    contact = models.IntegerField()

    class Meta:
        verbose_name_plural = ('Login')


class Payments(models.Model):
    user_id = models.IntegerField(null=True)
    mode = models.IntegerField(choices=TYPE)
    duration = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ('Payments')
