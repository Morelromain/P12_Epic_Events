from rest_framework import permissions

from user.models import User


class UserPermission(permissions.BasePermission):
    """
    BLABLA
    """

    def has_permission(self, request, view):
        """print(list(request.user.groups.filter()))"""
        if request.user.groups.filter(name="Management").exists():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Management").exists():
            return True
        return False
