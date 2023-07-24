from rest_framework import permissions
from rest_framework.request import HttpRequest

from .models.comment import Comment
from .models.news import News


class AuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(
            self, request: HttpRequest, view, obj: Comment | News
    ):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author_id == request.user.author_id
        )
