# Creating our models of the Admins
from django.db import models


class Administrators(models.Model):
    username = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='images/')
    email = models.EmailField()
    password = models.CharField(max_length=255)
    contact = models.IntegerField()

    class Meta:
        verbose_name_plural = ('Administrators')


class Drivers(models.Model):
    pass

    class Meta:
        verbose_name_plural = ('Drivers')


class Trucks(models.Model):
    pass

    class Meta:
        verbose_name_plural = ('Trucks')


class Pricings(models.Model):
    pass

    class Meta:
        verbose_name_plural = ('Pricings')


class Requests(models.Model):
    pass

    class Meta:
        verbose_name_plural = ('Requests')


class HelpCenter(models.Model):
    pass
