from rest_framework import permissions
from rest_framework.request import HttpRequest

from users.models.author import Author


class AuthorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            or request.user.is_superuser
        )

    def has_object_permission(self, request: HttpRequest, view, obj: Author):
        return (
            request.method in permissions.SAFE_METHODS
            or obj == request.user.author
            or request.user.is_superuser
        )
