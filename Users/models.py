# Creating our models from the Users
from django.db import models


class Users(models.Model):
    pass

    class Meta:
        verbose_name_plural = ('Users')


class Requests(models.Model):
    pass

    class Meta:
        verbose_name_plural = ('Requests')


class Payments(models.Model):
    pass

    class Meta:
        verbose_name_plural = ('Payments')


class HelpCenter(models.Model):
    pass
