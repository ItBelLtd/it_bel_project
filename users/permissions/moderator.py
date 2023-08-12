from rest_framework import permissions
from rest_framework.request import HttpRequest


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_moderator or request.user.is_superuser

    def has_object_permission(self, request: HttpRequest, view, obj):
        return request.user.is_moderator or request.user.is_superuser
