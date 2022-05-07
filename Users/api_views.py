# Creating our API views
from rest_framework import generics
from .models import User, Payments
from .serializers import UserSerializers, PaymentsSerializers
from Basemodel.models import Pricings, Requests, HelpCenter
from Admin.serializers import PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


"""
    List all the models instance or create a new model instance
"""


class Auth(APIView):
    def get_object(self, request):
        try:
            return User.objects.get(
                email=request.data['email'], password=request.data['password'])
        except User.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        Login_valid = self.get_object(request)
        if Login_valid is None:
            pass
        else:
            serializer = UserSerializers(Login_valid)
            id = serializer.data['id']
            return Response(id)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_list(generics.ListCreateAPIView):

    queryset = User.objects.all()
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
            return User.objects.get(
                id=request.data['id'])
        except User.DoesNotExist:
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
    queryset = User.objects.all()
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
