# Creating serializers of Admin Application
from rest_framework import serializers
from .models import Administrators, Drivers, Trucks, Pricings, Requests, HelpCenter


class AdministratorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrators
        fields = "__all__"


class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = "__all__"


class TrucksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trucks
        fields = "__all__"


class PricingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricings
        fields = "__all__"


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = "__all__"


class HelpCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpCenter
        fields = "__all__"
