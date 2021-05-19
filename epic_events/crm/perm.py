from rest_framework import permissions

from user.models import User


class ClientPermission(permissions.BasePermission):
    """
    BLABLA
    """

    def has_permission(self, request, view):
        """print(list(request.user.groups.filter()))"""
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
            """return request.method == "GET" #True pour get"""
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
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
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
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
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Management").exists():
            return True
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return True
        return False
