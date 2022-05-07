# Creating our API views
from rest_framework import generics
from .models import Users, Payments
from .serializers import UsersSerializers, PaymentsSerializers
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
            return Users.objects.get(
                email=request.data['email'], password=request.data['password'])
        except Users.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        user_valid = self.get_object(request)
        if user_valid is None:
            pass
        else:
            serializer = UsersSerializers(user_valid)
            id = serializer.data['id']
            return Response(id)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_list(generics.ListCreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UsersSerializers


"""
{
     "email": "akotobamfo.eab@gmail.com",
     "password": "laptop"
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
        user_valid = self.get_object(request)
        if user_valid is None:
            pass
        else:
            serializer = UsersSerializers(user_valid)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


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
