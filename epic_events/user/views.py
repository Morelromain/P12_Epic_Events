from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import User
from django.contrib.auth.models import Group

from .serializers import UserSerializer
from .serializers import GroupSerializer
from .perm import UserPermission, GroupPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [(UserPermission & permissions.IsAuthenticated)]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [(GroupPermission & permissions.IsAuthenticated)]
