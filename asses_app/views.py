from asses_app.models import Client
from django.http.response import HttpResponse
from django.shortcuts import render
from .serializer import ClientSerializer,ProjectSerializer,UserSerializer
from rest_framework import generics
from . models import Client, Project
def home(request):
    return HttpResponse("Django Rest Framework Based Operations")

class CreateUser(generics.CreateAPIView):
    serializer_class=UserSerializer

class CreateClient(generics.CreateAPIView):
    serializer_class=ClientSerializer

class ListClient(generics.ListAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

class RUDClient(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


class CreateProject(generics.CreateAPIView):
    serializer_class=ProjectSerializer

class RProject(generics.RetrieveAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer



