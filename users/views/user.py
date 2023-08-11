from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from ..models.follow import Follow
from ..models.user import User
from ..serializers.author import AuthorSerializer
from ..serializers.profile import ProfileSerializer
from ..serializers.users import (UserCreateSerializer, UserListSerializer,
                                 UserUpdateSerializer)
from users.permissions.user import UserOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [UserOwnerOrReadOnly, ]

    def create(self, request: HttpRequest, ):
        author_data = request.data.pop('author')
        if author_data:
            user_serializer = UserCreateSerializer(data=request.data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

            author_serializer = AuthorSerializer(data=author_data)
            author_serializer.is_valid(raise_exception=True)
            author_serializer.save(user=user)
            return Response(author_serializer.data, status=201)
        user_serializer = UserCreateSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data, status=201)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action in ('update', 'partial_update'):
            return UserUpdateSerializer
        return UserListSerializer

    @action(
        methods=['GET'],
        url_path='profile',
        detail=False,
        permission_classes=[UserOwnerOrReadOnly, ],
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
