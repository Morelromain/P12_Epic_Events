from rest_framework import permissions

from user.models import User


class UserPermission(permissions.BasePermission):
    """
    User permissions
    His own user : Update
    Other user : Read only
    """

    def has_permission(self, request, view):
        if request.method in ["PUT", "PATCH"]:
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False

class GroupPermission(permissions.BasePermission):
    """
    Group permissions, read only
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS