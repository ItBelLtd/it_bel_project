from rest_framework import permissions
from rest_framework.request import HttpRequest

from users.models.user import User


class UserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj: User):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        return obj.user_id == request.user.user_id or request.user.is_superuser
