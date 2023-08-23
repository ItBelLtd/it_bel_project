from django.conf import settings
from rest_framework import viewsets

from ..mixins.user import EmailConfirmResetPasswordMixin, UserMixin
from ..models.user import User
from ..serializers.users import (UserCreateSerializer, UserListSerializer,
                                 UserUpdateSerializer)
from ..services import send_email_verification
from users.permissions.user import UserOwnerOrReadOnly


class UserViewSet(
    viewsets.ModelViewSet,
    UserMixin,
    EmailConfirmResetPasswordMixin
):
    queryset = User.objects.all()
    permission_classes = [UserOwnerOrReadOnly, ]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action in ('update', 'partial_update'):
            return UserUpdateSerializer
        return UserListSerializer

    def perform_create(self, serializer: UserCreateSerializer):
        if not settings.IT_BEL_EMAIL_CONFIRMATION_ENABLED:
            serializer.save(is_active=True)
            return
        user = serializer.save()
        send_email_verification(user=user, viewset_instance=self)
