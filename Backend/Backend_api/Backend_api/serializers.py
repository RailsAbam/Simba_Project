
from email.headerregistry import Group
from importlib.metadata import files

from django.contrib.auth.models import Users
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['Username', 'name', 'Password']

        
        
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = []
