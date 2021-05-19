from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from user.models import User
from django.contrib.auth.models import Group
from user.serializers import UserSerializer
from user.serializers import GroupSerializer
from .perm import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission & permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
