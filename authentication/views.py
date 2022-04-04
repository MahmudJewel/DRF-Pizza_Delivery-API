from django.shortcuts import render
from authentication.serializers import UserSerializers
from authentication.models import User
from rest_framework import viewsets
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
