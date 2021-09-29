from django.shortcuts import render
from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer, LoginSerializer
from user.models import User

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            username = data.get('mobile')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:

            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

