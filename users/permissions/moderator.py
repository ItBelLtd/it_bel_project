from rest_framework import permissions
from rest_framework.request import HttpRequest


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_moderator:
            return True
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request: HttpRequest, view, obj):
        if request.user.is_moderator:
            return True
        if request.user.is_superuser:
            return True
        return False
