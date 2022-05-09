# Creating our models from the Login
from django.db import models
from Basemodel.models import TYPE, DAYS
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(models.Model):
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

        verbose_name_plural = ('Users')


class Payments(models.Model):
    user_id = models.IntegerField(null=True)
    mode = models.IntegerField(choices=TYPE)
    duration = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ('Payments')
