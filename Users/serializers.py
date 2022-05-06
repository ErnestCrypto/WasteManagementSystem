# Creating our serializers
from rest_framework import serializers
from .models import Login, Payments


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
