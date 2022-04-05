# Registering our models
from django.contrib import admin
from .models import Administrators, Drivers, Trucks, Pricings, Requests, HelpCenter


@admin.register(Administrators)
class AdministratorAdmin(admin.ModelAdmin):
    pass


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    pass


@admin.register(Trucks)
class TrucksAdmin(admin.ModelAdmin):
    pass


@admin.register(Pricings)
class PricingAdmin(admin.ModelAdmin):
    pass


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    pass


@admin.register(HelpCenter)
class HelpCenterAdmin(admin.ModelAdmin):
    pass
