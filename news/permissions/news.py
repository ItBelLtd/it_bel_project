from rest_framework import permissions
from rest_framework.request import HttpRequest

from news.models.comment import Comment
from news.models.news import News


class AuthorOrReadOnlyNews(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            or request.user.is_superuser
        )

    def has_object_permission(
            self, request: HttpRequest, view, obj: Comment | News
    ):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated and obj.author == request.user.author
        )
