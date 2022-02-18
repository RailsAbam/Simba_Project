from django.contrib.auth.models import Users
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['Username', 'name', 'Password']
        