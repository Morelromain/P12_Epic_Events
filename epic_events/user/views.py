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
    '''permission_classes = [(UserPermission & permissions.IsAuthenticated) | permissions.IsAdminUser]'''
    permission_classes = [(UserPermission & permissions.IsAuthenticated)]
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
