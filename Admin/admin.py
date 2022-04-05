# Registering our models
from django.contrib import admin
from .models import Administrators, Drivers, Trucks


@admin.register(Administrators)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'profile', 'email', 'password', 'contact',
    ]


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'profile', 'firstname', 'lastname', 'email', 'contact', 'day', 'location', 'truck_id',
    ]


@admin.register(Trucks)
class TrucksAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'driver_id', 'number_plate',  'details',
    ]
