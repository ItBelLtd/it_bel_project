from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest, Request
from rest_framework.response import Response

from ..models.follow import Follow
from ..models.user import User
from ..serializers.author import AuthorSerializer
from ..serializers.profile import ProfileSerializer
from users.permissions.user import UserOwnerOrReadOnly
from users.services import (get_user_id_from_cache, send_email_reset_password,
                            send_email_verification, validate_email)


class UserMixin:
    @action(
        methods=['GET'],
        url_path='profile',
        detail=False,
        permission_classes=[UserOwnerOrReadOnly, IsAuthenticated, ],
    )
    def profile(self, request: HttpRequest):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    @profile.mapping.patch
    def update_my_model(self, request: HttpRequest):
        serializer = ProfileSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @profile.mapping.delete
    def profile_delete(self, request: HttpRequest):
        serializer = ProfileSerializer(request.user)
        serializer.destroy()
        return Response({'detail': 'Success'}, status=204)

    @action(
        methods=['GET', ],
        detail=True,
        url_path='following',
    )
    def user_following_list(self, request: HttpRequest, pk: int):
        user = get_object_or_404(User, user_id=pk)
        following_authors = []
        for i in Follow.objects.filter(follower=user):
            following_authors.append(i.author)
        serializer = AuthorSerializer(following_authors, many=True)

        return Response(serializer.data)


class EmailConfirmationPasswordRest:

    def get_user_for_confirm(self, user_id):
        try:
            user = self.get_queryset().get(pk=user_id)
            return user
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(
                'User not found',
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(
        methods=['GET', ],
        url_path='confirm',
        detail=False,
        url_name='confirm',
    )
    def confirm(self, request: Request):
        user_id = get_user_id_from_cache(
            request.query_params.get('confirmation_token', ''),
            prefix_key=settings.IT_BEL_USER_CONFIRMATION_KEY
        )
        if not user_id:
            return Response(
                'Token is invalid or expired. Please request/'
                ' another confirmation email by signing in.',
                status=status.HTTP_400_BAD_REQUEST
            )
        user: User = self.get_user_for_confirm(user_id=user_id)

        user.is_active = True
        user.save()
        return Response(
            'Email successfully confirmed',
            status=status.HTTP_200_OK
        )

    @action(
        methods=['POST', ],
        url_path='resend-confirmation-email',
        detail=False,
        url_name='resend-confirmation-email',
    )
    def resend_confirmation_email(self, request: Request):
        email = request.data.get('email', '')
        if not email:
            return Response(
                'Email not found',
                status=status.HTTP_400_BAD_REQUEST
            )
        user_email = validate_email(email=request.data.get('email', ''))
        user: User = self.get_queryset().filter(email=user_email).first()
        if not user:
            return Response(
                'User not found',
                status=status.HTTP_400_BAD_REQUEST
            )
        send_email_verification(
            user=user,
            viewset_instance=self
        )
        return Response(
            'Confirmation email sent',
            status=status.HTTP_200_OK
        )

    @action(
        methods=['POST', ],
        url_path='reset-password',
        detail=False,
        url_name='reset-password',
    )
    def reset_password(self, request: Request):
        user_email = validate_email(email=request.data.get('email', ''))
        if not user_email:
            return Response(
                'Email not found',
                status=status.HTTP_400_BAD_REQUEST
            )
        user: User = self.get_queryset().filter(email=user_email).first()
        if not user:
            return Response(
                'User not found',
                status=status.HTTP_400_BAD_REQUEST
            )

        send_email_reset_password(
            user=user,
            viewset_instance=self
        )
        return Response(
            'Confirmation email sent',
            status=status.HTTP_200_OK
        )

    @action(
        methods=['POST', ],
        url_path='reset-password-confirm',
        detail=False,
        url_name='reset-password-confirm',

    )
    def reset_password_confirm(self, request: Request):
        user_id = get_user_id_from_cache(
            request.query_params.get('confirmation_token', ''),
            prefix_key=settings.IT_BEL_PASSWORD_RESET_CODE
        )
        if not user_id:
            return Response(
                'Token is invalid or expired. Please request/'
                ' another confirmation email by signing in.',
                status=status.HTTP_400_BAD_REQUEST
            )
        user: User = self.get_user_for_confirm(user_id=user_id)

        return Response(
            {'msg': 'Email confirmed', 'user_id': user.pk},
            status=status.HTTP_200_OK
        )

    @action(
        methods=['POST', ],
        url_path='set-new-password',
        detail=False,
        url_name='set-new-password',

    )
    def set_new_password(self, request: Request):
        user_id = request.data.get('user_id', '')
        new_password = request.data.get('new_password', '')
        if not user_id or not new_password:
            return Response(
                'User_id or new_password not found',
                status=status.HTTP_400_BAD_REQUEST
            )
        user: User = self.get_user_for_confirm(user_id=user_id)
        password_confirm = request.data.get('password_confirm', '')
        if new_password != password_confirm:
            return Response(
                'Passwords do not match',
                status=status.HTTP_400_BAD_REQUEST
            )
        user.set_password(new_password)
        user.save()
        return Response(
            'Password changed',
            status=status.HTTP_200_OK
        )
