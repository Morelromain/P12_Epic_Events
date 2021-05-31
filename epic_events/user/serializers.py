from rest_framework import serializers

from user.models import User
from django.contrib.auth.models import Group


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name',
        'email', 'is_staff', 'last_login', 'groups']
        read_only_fields = ('last_login', 'is_staff')