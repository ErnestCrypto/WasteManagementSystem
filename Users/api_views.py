# Creating our API views
from rest_framework import generics
from .models import Users, Payments
from .serializers import UsersSerializers, PaymentsSerializers
from Basemodel.models import Pricings, Requests, HelpCenter
from Admin.serializers import PricingsSerializer, RequestsSerializer, HelpCenterSerializer

"""
    List all the models instance or create a new model instance
"""


class Users_list(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
