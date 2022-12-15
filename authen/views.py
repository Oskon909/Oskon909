from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializers import RegistrationSerializer


# Create your views here.

class RegistrationApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer