# Creating our API views
import datetime
import jwt
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import AdministratorsSerializer, DriversSerializer, TrucksSerializer, PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from .models import Administrators, Drivers, Trucks
from Basemodel.models import Pricings, Requests, HelpCenter
from django.http import Http404
""" 
Making Get and Post requests
List all models instances or create a new instance
"""


class Create(generics.ListCreateAPIView):
    queryset = Administrators.objects.all()
    serializer_class = AdministratorsSerializer


class Auth(APIView):
    def get_object(self, request):
        try:
            admin = Administrators.objects.get(
                email=request.data['email'], password=request.data['password'])
            return admin
        except Administrators.DoesNotExist:
            raise Http404

    def post(self, request, format=None):

        Login_valids = self.get_object(request)

        if Login_valids is None:
            pass
        else:
            serializer = AdministratorsSerializer(Login_valids)
            payload = {
                'id': Login_valids.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret',
                               algorithm='HS256').decode('utf-8')
            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'id': serializer.data['id'],
                'jwt': token
            }

            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoggedInUsers(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized user')
        admin = Administrators.objects.filter(id=payload['id']).first()
        serializer = AdministratorsSerializer(admin)
        return Response(serializer.data)


class Logout(APIView):
    def post(self, request, format=None):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logout successful'
        }
        return response


class Adminstrators_list(APIView):
    def get(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            admin = Administrators.objects.all()
            serializer = AdministratorsSerializer(admin, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            serializer = AdministratorsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Drivers_list(generics.ListCreateAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


class Trucks_list(generics.ListCreateAPIView):
    queryset = Trucks.objects.all()
    serializer_class = TrucksSerializer


class Pricings_list(generics.ListCreateAPIView):
    queryset = Pricings.objects.all()
    serializer_class = PricingsSerializer


class Requests_list(generics.ListCreateAPIView):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer


class HelpCenter_list(generics.ListCreateAPIView):
    queryset = HelpCenter.objects.all()
    serializer_class = HelpCenterSerializer

    """
    Making GET, PUT and DELETE
    Retrive, update and destory model instances
    """


class Adminstrators_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrators.objects.all()
    serializer_class = AdministratorsSerializer


class Drivers_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


class Trucks_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trucks.objects.all()
    serializer_class = TrucksSerializer


class Pricings_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pricings.objects.all()
    serializer_class = PricingsSerializer


class Requests_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer


class HelpCenter_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = HelpCenter.objects.all()
    serializer_class = HelpCenterSerializer
