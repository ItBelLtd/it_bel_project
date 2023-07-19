from django.http import HttpRequest
from rest_framework import permissions

from .models.author import Author
from .models.user import User


class UserOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_superuser
        return True

    def has_object_permission(self, request: HttpRequest, view, obj: User):
        return (
                (request.user and request.user.is_superuser)
                or obj.user_id == request.user.user_id
        )


class AuthorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
        )

    def has_object_permission(self, request: HttpRequest, view, obj: Author):
        return (
                request.method in permissions.SAFE_METHODS
                or obj.author_id == request.user.author_id
                or (request.user and request.user.is_superuser)
        )


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsModerate(permissions.BasePermission):

    def has_permission(self, request, view):
        return ((request.user and request.user.is_moderator)
                or (request.user and request.user.is_superuser))
