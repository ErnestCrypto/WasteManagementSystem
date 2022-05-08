# Creating our API views
from rest_framework import generics
from .models import Users, Payments
from .serializers import UserSerializers, PaymentsSerializers
from Basemodel.models import Pricings, Requests, HelpCenter
from Admin.serializers import PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

"""
    List all the models instance or create a new model instance
"""


class Test(APIView):

    def get_object(self, request):
        try:
            return Users.objects.get(
                email=request.data['email'], password=request.data['password'])
        except Users.DoesNotExist:
            raise Http404

    def post(self, request, format=None):

        Login_valids = self.get_object(request)
        if Login_valids is None:
            pass
        else:
            serializer = UserSerializers(Login_valids)

            return Response({
                            'id': serializer.data['id'],
                            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, format=None):
    #     users = Users.objects.all()
    #     serializer = UserSerializers(users, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = UserSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Auth(APIView):

    def get_object(self, request):
        try:
            return Users.objects.get(
                email=request.data['email'], password=request.data['password'])
        except Users.DoesNotExist:
            raise Http404

    def post(self, request, format=None):

        Login_valids = self.get_object(request)
        if Login_valids is None:
            pass
        else:
            serializer = UserSerializers(Login_valids)

            return Response({
                            'id': serializer.data['id'],
                            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_list(generics.ListCreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UserSerializers


"""
{
     "email": "akotobamfo.eab@gmail.com",
     "password": "laptop"
}

{
     "id": "1"
    
}
"""


class Payments_list(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers


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
    Retrieve, Update and destroy model instances.
    """


class Auth_details(APIView):
    def get_object(self, request):
        try:
            return Users.objects.get(
                id=request.data['id'])
        except Users.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        Login_valid = self.get_object(request)
        if Login_valid is None:
            pass
        else:
            serializer = UserSerializers(Login_valid)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


class Payments_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializers


class Pricings_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pricings.objects.all()
    serializer_class = PricingsSerializer


class Requests_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer


class HelpCenter_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = HelpCenter.objects.all()
    serializer_class = HelpCenterSerializer
