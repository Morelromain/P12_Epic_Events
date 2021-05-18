from django.shortcuts import render
from rest_framework import viewsets

from user.models import User
from django.contrib.auth.models import Group
from user.serializers import UserSerializer
from user.serializers import GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
