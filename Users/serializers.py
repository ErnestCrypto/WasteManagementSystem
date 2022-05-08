# Creating our serializers
from rest_framework import serializers
from Users.models import Users, Payments


class UserSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Users
        fields = "__all__"


class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
