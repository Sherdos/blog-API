from django.shortcuts import render
from rest_framework import generics
from apps.users.models import User 
from apps.users.serializers import UserSerializer, RegisterSerializer, UpdateSerializer

# Create your views here.
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateSerializer

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
