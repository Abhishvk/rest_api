from django.db import models
from rest_framework import serializers
from . models import User,Client,Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'