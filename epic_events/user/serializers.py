from rest_framework import serializers

from .models import User
from django.contrib.auth.models import Group


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url','name']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'first_name', 'last_name',
        'email', 'is_staff', 'last_login', 'groups']
        read_only_fields = ('last_login', 'is_staff', 'groups', 'password', 'username')
