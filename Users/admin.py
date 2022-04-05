# Registering our models
from django.contrib import admin
from .models import Users, Requests, Payments, HelpCenter


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    pass


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    pass


@admin.register(HelpCenter)
class HelpCenterAdmin(admin.ModelAdmin):
    pass
