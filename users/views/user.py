from rest_framework import viewsets

from ..mixins.user import UserMixin
from ..models.user import User
from ..serializers.users import (UserCreateSerializer, UserListSerializer,
                                 UserUpdateSerializer)
from users.permissions.user import UserOwnerOrReadOnly

import json


class UserViewSet(
    viewsets.ModelViewSet,
    UserMixin
):
    queryset = User.objects.all()
    permission_classes = [UserOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action in ('update', 'partial_update'):
            return UserUpdateSerializer
        return UserListSerializer
