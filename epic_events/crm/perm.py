from rest_framework import permissions

from user.models import User


class ClientPermission(permissions.BasePermission):
    """
    Client permissions based on user group :
    User Sales : All permissions
    Support Sales : Read only
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False


class ContractPermission(permissions.BasePermission):
    """
    Contract permissions based on the user group :
    User Sales : All permissions
    Support Sales : Read only
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False


class EventPermission(permissions.BasePermission):
    """
    Contract permissions based on the user group :
    User Sales : All permissions
    Support Sales : Update for its own events, read for other
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists() and obj.accomplish == False :
            if request.user == obj.support_contact:
                return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
            else:
                return request.method in permissions.SAFE_METHODS
        return False
