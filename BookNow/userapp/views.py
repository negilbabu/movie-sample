import jwt
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serialize import UserSerialize, LoginSerialize
from rest_framework import status
from .models import UserModel
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.http import HttpResponse

class UserView(APIView):
    user_serializer = UserSerialize

    def post(self, request):
        data = request.data
        email = request.data.get('email')
        serializer = self.user_serializer(data=data)
        if serializer.validate(data):
            if serializer.is_valid():
                user = UserModel.objects.filter(email=email).first()
                if user:
                    raise AuthenticationFailed({
                        'errorCode': '1008',
                        'message': email + ' Already Exists'
                    })
                serializer.save()

                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'errorCode': "4000", 'Message': "Error"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    login_serializer = LoginSerialize

    def post(self, request):
        data = request.data
        email = request.data.get('email')
        password = request.data.get('password')
        serializer = self.login_serializer(data=data)
        if serializer.validate(data):
            user = UserModel.objects.filter(email=email).first()
            if not user:
                raise AuthenticationFailed({
                    'errorCode': '4000',
                    'message': email + ' Not Found'
                })

        if not user or not check_password(password, user.password):
            raise AuthenticationFailed({
                'errorCode': '4001',
                'message': 'Password is wrong for ' + email
            })

        access_token_payload = {
            'user_id': user.id,
            'email': user.email,
            'name': user.name,
            'exp': datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION)
        }

        access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256')

        refresh_token_payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRATION)
        }

        refresh_token = jwt.encode(refresh_token_payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({
            'user_id': user.id,
            'email': user.email,
            'name': user.name,
            'access_token': access_token,
            'refresh_token': refresh_token,
        })
