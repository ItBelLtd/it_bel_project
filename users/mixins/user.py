from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from ..models.follow import Follow
from ..models.user import User
from ..permissions.user import UserOwnerOrReadOnly
from ..serializers.author import AuthorSerializer
from ..serializers.users import UserListSerializer


class UserMixin:
    @extend_schema(tags=['profile'])
    @action(
        methods=['GET'],
        url_path='profile',
        detail=False,
        permission_classes=[UserOwnerOrReadOnly, IsAuthenticated, ],
    )
    def profile(self, request: Request):
        serializer = UserListSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(tags=['profile'])
    @profile.mapping.patch
    def profile_update(self, request: Request):
        serializer = UserListSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @extend_schema(tags=['profile'])
    @profile.mapping.delete
    def profile_delete(self, request: Request):
        user: User = request.user
        user.delete()
        return Response({'detail': 'Success'}, status=204)

    @action(
        methods=['GET', ],
        detail=True,
        url_path='following',
    )
    def user_following_list(self, request: Request, pk: int):
        # Can be refactored with related names
        user = get_object_or_404(User, user_id=pk)
        following_authors = []
        for i in Follow.objects.filter(follower=user):
            following_authors.append(i.author)
        serializer = AuthorSerializer(following_authors, many=True)

        return Response(serializer.data)
