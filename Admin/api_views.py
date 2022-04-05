# Creating our API views
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdministratorsSerializer, DriversSerializer, TrucksSerializer, PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from .models import Administrators, Drivers, Trucks
from Basemodel.models import Pricings, Requests, HelpCenter

# Making Get and Post requests


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
