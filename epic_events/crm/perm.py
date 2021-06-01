from rest_framework import permissions

from user.models import User



class ClientPermission(permissions.BasePermission):
    """
    BLABLA
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return False
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

class ContractPermission(permissions.BasePermission):
    """
    BLABLA
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

class EventPermission(permissions.BasePermission):
    """
    BLABLA
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            if request.user == obj.support_contact:
                return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
            else:
                return request.method in permissions.SAFE_METHODS
        return False
