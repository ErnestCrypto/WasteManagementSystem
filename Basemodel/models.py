# Creating the basemodels
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


class Pricings(models.Model):
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=None, null=True)
    type = models.IntegerField(choices=TYPE, default=None)

    class Meta:
        verbose_name_plural = ('Pricings')


class Requests(models.Model):
    user_id = models.IntegerField(default=None, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=None)

    class Meta:
        verbose_name_plural = ('Requests')


class HelpCenter(models.Model):
    user_id = models.IntegerField(default=None, null=True)
    message = models.TextField(default=None)
    date_time = models.DateTimeField(auto_now_add=True)
