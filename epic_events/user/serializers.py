from rest_framework import serializers

from user.models import User
from django.contrib.auth.models import Group


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'groups']
