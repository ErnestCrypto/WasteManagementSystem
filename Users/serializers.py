# Creating our serializers
from rest_framework import serializers
from .models import Users, Payments


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
