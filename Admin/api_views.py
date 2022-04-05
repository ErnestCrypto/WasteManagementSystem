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


@api_view(['GET', 'POST'])
class Adminstrators_details(APIView):
    # If request is a Get method
    def get(self, request):
        administrators = Administrators.objects.all()
        serializer = AdministratorsSerializer(administrators, many=True)
        return Response(serializer.data)
