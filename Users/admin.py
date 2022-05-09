# Registering our models
from django.contrib import admin
from Users.models import User, Payments


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
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
