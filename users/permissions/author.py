from rest_framework import permissions
from rest_framework.request import HttpRequest

from users.models.author import Author


class AuthorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request: HttpRequest, view, obj: Author):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj == request.user.author:
            return True
        if request.user.is_superuser:
            return True
        return False
