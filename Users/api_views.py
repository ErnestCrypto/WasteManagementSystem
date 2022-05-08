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
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


"""
    List all the models instance or create a new model instance
"""
"""
if request.method == 'POST':
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(request.user)
    token = jwt_encode_handler(payload)
    return HttpResponse('Get token auth request and data is as: {}'.format(token))
"""


class Test(APIView):
    permission_classes = (AllowAny,)

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

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
            user = serializer.data['id']

            return Response({
                            'id': serializer.data['id'],

                            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    {
        "email": "akotobamfo.eab@gmail.com",
        "password": "laptop"
    }

{
     "id": "1"
    
}
"""


class Auth(APIView):

    def get_object(self, request):
        try:
            return Users.objects.get(
                email=request.data['email'], password=request.data['password'])
        except Users.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)
        Login_valids = self.get_object(request)
        if Login_valids is None:
            pass
        else:
            serializer = UserSerializers(Login_valids)

            return Response({
                            'id': serializer.data['id'],
                            'token': token
                            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_list(generics.ListCreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UserSerializers


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
