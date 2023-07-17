from rest_framework import permissions


class UserOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_staff)
        else:
            return True

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS and bool(
            request.user and request.user.is_staff)) or obj.user_id == request.user.user_id


class AuthorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author_id == request.user.author_id
