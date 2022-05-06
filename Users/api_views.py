# Creating our API views
from rest_framework import generics
from .models import Login, Payments
from .serializers import LoginSerializers, PaymentsSerializers
from Basemodel.models import Pricings, Requests, HelpCenter
from Admin.serializers import PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


"""
    List all the models instance or create a new model instance
"""


class Login_list(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializers


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
    Retrieve, Update and destroy model instsnces.
    """


class Login_details(APIView):
    def get_object(self, pk):
        try:
            return Login.objects.get(firstname=pk)
        except Login.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Login = self.get_object(pk)
        serializer = LoginSerializers(Login)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Login = self.get_object(pk)
        serializer = LoginSerializers(Login, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Login = self.get_object(pk)
        Login.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
