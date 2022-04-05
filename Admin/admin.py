# Registering our models
from django.contrib import admin
from .models import Administrators, Drivers, Trucks, Pricings, Requests, HelpCenter


@admin.register(Administrators)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'profile', 'email', 'password', 'contact',
    ]


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    list_display = [
        'id',  'firstname', 'lastname', 'email', 'contact', 'day', 'location', 'truck_id',
    ]


@admin.register(Trucks)
class TrucksAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'driver_id', 'number_plate',  'details',
    ]


@admin.register(Pricings)
class PricingAdmin(admin.ModelAdmin):
    list_display = [
        'id',  'price', 'type',
    ]


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user_id', 'date_time',  'status',
    ]


@admin.register(HelpCenter)
class HelpCenterAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user_id', 'message', 'date_time',
    ]
