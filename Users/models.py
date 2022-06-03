# Creating our models from the Login
from django.db import models
from Basemodel.models import TYPE, DAYS


class User(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    pricing = models.CharField(max_length=255)
    day = models.IntegerField(choices=DAYS, default=None)
    balance = models.CharField(max_length=255)
    profile = models.ImageField(
        upload_to='images/', null=True, blank=True, default=None)
    contact = models.TextField(default=None)

    class Meta:
        verbose_name_plural = ('Users')


class Payments(models.Model):
    user_id = models.IntegerField(null=True)
    mode = models.IntegerField(choices=TYPE)
    duration = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ('Payments')


class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='User',
                             on_delete=models.CASCADE, blank=True, default=None, null=True)
    durationStart = models.IntegerField(default=None)
    durationEnd = models.IntegerField(default=None)
    name = models.CharField(max_length=255, default=None)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None)
