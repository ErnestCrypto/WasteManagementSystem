# Creating our API views
from rest_framework import generics
from .models import User, Payments
from .serializers import UserSerializers, PaymentsSerializers
from Basemodel.models import Pricings, Requests, HelpCenter
from Admin.serializers import PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.authtoken.models import Token
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
from datetime import timedelta
import jwt
import datetime

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

    def get_object(self, request):
        try:
            return User.objects.get(
                email=request.data['email'], password=request.data['password'])
        except User.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class Login(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthorized user')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized user')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializers(user)

        return Response(serializer.data)


class Logout(APIView):
    def post(self, request, format=None):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logout successful'
        }
        return response


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
    permission_classes = (AllowAny,)

    def get_object(self, request):
        try:
            user = User.objects.get(
                email=request.data['email'], password=request.data['password'])
            return user
        except User.DoesNotExist:
            raise Http404

    def post(self, request, format=None):

        Login_valids = self.get_object(request)

        if Login_valids is None:
            pass
        else:
            serializer = UserSerializers(Login_valids)
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


class User_list(generics.ListCreateAPIView):

    queryset = User.objects.all()
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
