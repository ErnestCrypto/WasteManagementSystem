# registring our basemodels
from django.contrib import admin
from .models import Pricings, Requests, HelpCenter


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
