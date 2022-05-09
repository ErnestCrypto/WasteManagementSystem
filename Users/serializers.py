# Creating our serializers
from rest_framework import serializers
from Users.models import User, Payments


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
