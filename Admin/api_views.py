# Creating our API views
from rest_framework import generics
from .serializers import AdministratorsSerializer, DriversSerializer, TrucksSerializer, PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from .models import Administrators, Drivers, Trucks
from Basemodel.models import Pricings, Requests, HelpCenter

""" 
Making Get and Post requests
List all models instances or create a new instance
"""


class Adminstrators_details(generics.ListCreateAPIView):
    queryset = Administrators.objects.all()
    serializer_class = AdministratorsSerializer


class Drivers_details(generics.ListCreateAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


class Trucks_details(generics.ListCreateAPIView):
    queryset = Trucks.objects.all()
    serializer_class = TrucksSerializer


class Pricings_details(generics.ListCreateAPIView):
    queryset = Pricings.objects.all()
    serializer_class = PricingsSerializer


class Requests_details(generics.ListCreateAPIView):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer


class HelpCenter_details(generics.ListCreateAPIView):
    queryset = HelpCenter.objects.all()
    serializer_class = HelpCenterSerializer

    """
    Making GET, PUT and DELETE
    Retrive, update and destory model instances
    """


class Adminstrators_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrators.objects.all()
    serializer_class = AdministratorsSerializer
