from rest_framework import permissions


class ClientPermission(permissions.BasePermission):
    """
    Client permissions based on user group :
    User Sales :    All permissions if not converted,
                    All permissions without delete else.
    User Support : Read only
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            if obj.converted is False:
                return True
            else:
                return request.method in [
                    "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False


class ContractPermission(permissions.BasePermission):
    """
    Contract permissions based on the user group :
    User Sales :    All permissions if not ratified,
                    Read only else.
    User Support : Read only
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return True
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            if (request.user == obj.sales_contact and
                    obj.ratified is False):
                return True
            else:
                return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False


class EventPermission(permissions.BasePermission):
    """
    Contract permissions based on the user group :
    User Sales : All permissions
    User Support :  Update for its own events if not accomplish,
                    Read only else.
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            return request.method in [
                "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            if (request.user == obj.support_contact and
                    obj.accomplish is False):
                return request.method in [
                    "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
            else:
                return request.method in permissions.SAFE_METHODS
        return False


class StatusPermission(permissions.BasePermission):
    """
    Status permissions :
    Read only for User Sales and Supports
    """

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Sales").exists():
            return request.method in permissions.SAFE_METHODS
        if request.user.groups.filter(name="Support").exists():
            return request.method in permissions.SAFE_METHODS
        return False
