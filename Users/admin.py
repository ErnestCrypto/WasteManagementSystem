# Registering our models
from django.contrib import admin
from Users.models import Users, Payments


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
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
