from rest_framework import permissions
from rest_framework.request import HttpRequest

from news.models.comment import Comment
from news.models.news import News


class AuthorOrReadOnlyComments(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view):
        if request.user.is_authenticated:
            return True
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(
            self, request: HttpRequest, view, obj: Comment | News
    ):
        if obj.author == request.user:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return False
