from rest_framework import permissions
from rest_framework.request import HttpRequest


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request: HttpRequest, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return False
