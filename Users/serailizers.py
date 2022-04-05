# Creating our serializers
from rest_framework import serializers
from .models import Users, Payments


class UsersSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class PaymentsSerailizers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
