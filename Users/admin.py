# Registering our models
from django.contrib import admin
from .models import Login, Payments


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'firstname', 'lastname',
        'address', 'email', 'password', 'pricing',
        'day', 'balance', 'profile', 'contact',

    ]


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user_id', 'mode', 'duration', 'amount', 'date_time',
    ]
