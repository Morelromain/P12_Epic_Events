from rest_framework import permissions

from user.models import User


class UserPermission(permissions.BasePermission):
    """
    BLABLA
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.method == "PUT":
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        if request.user.groups.filter(name="Management").exists():
            return True
        return False
