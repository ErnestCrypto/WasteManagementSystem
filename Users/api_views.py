# Creating our API views
from rest_framework import generics
from .models import User, Payments
from .serializers import UserSerializers, PaymentsSerializers
from Basemodel.models import Pricings, Requests, HelpCenter
from Admin.serializers import PricingsSerializer, RequestsSerializer, HelpCenterSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.permissions import AllowAny
import jwt
import datetime

"""
    List all the models instance or create a new model instance
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


class LoggedInUsers(APIView):
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


class User_list(APIView):

    def get(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            user = User.objects.all()
            serializer = UserSerializers(user, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            serializer = UserSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Payments_list(APIView):
    def get(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            payment = Payments.objects.all()
            serializer = PaymentsSerializers(payment, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            serializer = PaymentsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Pricings_list(APIView):
    def get(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            pricing = Pricings.objects.all()
            serializer = PricingsSerializer(pricing, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            serializer = PricingsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Requests_list(APIView):
    def get(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            request = Requests.objects.all()
            serializer = RequestsSerializer(request, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            serializer = RequestsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelpCenter_list(APIView):
    def get(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            help = HelpCenter.objects.all()
            serializer = HelpCenterSerializer(help, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user')
        else:
            serializer = HelpCenterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthorized user!')
        else:
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
