# Creating our models of the Admins
from django.db import models

DAYS = [
    (1, 'MONDAY'),
    (2, 'TUESDAY'),
    (3, 'WEDNESDAY'),
    (4, 'THURSDAY'),
    (5, 'FRIDAY'),
    (6, 'SATURDAY'),
    (7, 'SUNDAY'),
]

TYPE = [
    (1, 'one time payment'),
    (2, 'subscription'),
]

STATUS = [
    (1, 'Pending'),
    (2, 'Approved'),
]


class Administrators(models.Model):
    username = models.CharField(max_length=255, default=None, null=True)
    profile = models.ImageField(upload_to='images/', default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=255, default=None)
    contact = models.IntegerField(default=None)

    class Meta:
        verbose_name_plural = ('Administrators')

    def __str__(self):
        return self.username


class Drivers(models.Model):
    firstname = models.CharField(max_length=255, default=None, null=True)
    lastname = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    contact = models.IntegerField(default=None)
    day = models.CharField(max_length=255, choices=DAYS, default=None)
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


class Pricings(models.Model):
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=None, null=True)
    type = models.CharField(max_length=255, choices=TYPE, default=None)

    class Meta:
        verbose_name_plural = ('Pricings')


class Requests(models.Model):
    user_id = models.IntegerField(default=None, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS, default=None)

    class Meta:
        verbose_name_plural = ('Requests')


class HelpCenter(models.Model):
    user_id = models.IntegerField(default=None, null=True)
    message = models.TextField(default=None)
    date_time = models.DateTimeField(auto_now_add=True)
