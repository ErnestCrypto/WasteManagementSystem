# Registering our models
from django.contrib import admin
from Users.models import User, Payments, Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        'durationStart',
        'durationEnd',
        'name',
        'price',
    ]


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
