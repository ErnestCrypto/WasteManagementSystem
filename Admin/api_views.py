# Creating our API views
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdministratorsSerializer, DriversSerializer, TrucksSerializer, PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from .models import Administrators, Drivers, Trucks
from Basemodel.models import Pricings, Requests, HelpCenter

""" 
Making Get and Post requests
List all models instances or create a new instance
"""


class Adminstrators_details(APIView):
    # If request is a Get method
    def get(self, request, format=None):
        administrators = Administrators.objects.all()
        serializer = AdministratorsSerializer(administrators, many=True)
        return Response(serializer.data)

    # If request is a POST method
    def post(self, request, format=None):
        serializer = AdministratorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Drivers_details(APIView):
    # if request is a get method
    def get(self, request, format=None):
        drivers = Drivers.objects.all()
        serializer = DriversSerializer(drivers, many=True)
        return Response(serializer.data)

    # if request is a post method
    def post(self, request, format=None):
        serializer = DriversSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Trucks_details(APIView):
    # if request is a get method
    def get(self, request, format=None):
        trucks = Trucks.objects.all()
        serializers = TrucksSerializer(trucks, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = TrucksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
