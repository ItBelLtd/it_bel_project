from rest_framework import permissions
from rest_framework.request import HttpRequest

from .models.author import Author
from .models.user import User


class UserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj: User):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        return obj.user_id == request.user.user_id or request.user.is_superuser


class AuthorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request: HttpRequest, view, obj: Author):
        return (
            request.method in permissions.SAFE_METHODS
            or obj == request.user.author
        )


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request: HttpRequest, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_superuser


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_moderator or request.user.is_superuser

    def has_object_permission(self, request: HttpRequest, view, obj):
        return request.user.is_moderator or request.user.is_superuser
