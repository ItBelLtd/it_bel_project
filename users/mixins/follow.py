from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from ..models.author import Author
from ..models.follow import Follow
from ..serializers.follow import FollowSerializer
from ..serializers.users import UserListSerializer


class FollowMixin:
    @action(
        methods=['POST', ],
        detail=True,
        url_path='follow',
    )
    def follow(self, request: HttpRequest, pk: int):
        author = get_object_or_404(Author, author_id=pk)
        data = {
            'author': author.author_id,
            'follower': self.request.user.user_id,
        }
        serializer = FollowSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'CREATED'}, status=201)

    @action(
        methods=['POST', ],
        detail=True,
        url_path='unfollow',
    )
    def unfollow(self, request: HttpRequest, pk: int):
        author = get_object_or_404(Author, author_id=pk)
        follow = Follow.objects.filter(
            follower=self.request.user,
            author=author
        )
        follow.delete()
        return Response({'detail': 'NO_CONTENT'}, status=204)

    @action(
        methods=['GET', ],
        detail=True,
        url_path='followers',
    )
    def author_follower_list(self, request: HttpRequest, pk: int):
        get_object_or_404(Author, author_id=pk)
        followers = [i.follower for i in Follow.objects.filter(author=pk)]
        serializer = UserListSerializer(followers, many=True)
        return Response(serializer.data)
