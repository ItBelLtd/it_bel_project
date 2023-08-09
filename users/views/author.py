from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from ..models.author import Author
from ..models.follow import Follow
from ..serializers.author import AuthorSerializer
from ..serializers.follow import FollowSerializer
from ..serializers.users import UserListSerializer
from news.serializers.news import NewsSerializer
from users.permissions.author import AuthorOwnerOrReadOnly
from users.permissions.moderator import IsModerator


# We remove the inherited CreateModelMixin
# and DestroyModelMixin from the ModelViewSet,
# since these are methods for the user
# Check rest_framework/viewsets.py
class AuthorViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AuthorOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['surname', 'name']

    @action(
        methods=['GET', ],
        detail=True,
        url_path='news',
    )
    def get_author_news(self, request: HttpRequest, pk: int):
        author = get_object_or_404(Author, author_id=pk)
        news = author.news.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

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

    @action(
        detail=False,
        methods=['GET', ],
        url_path='author_stats',
        permission_classes=[IsModerator, ]
    )
    def registration_counts(self, request: HttpRequest):
        today = timezone.now().date()
        week_start = today - timezone.timedelta(days=today.weekday())
        month_start = today.replace(day=1)

        today_count = self.queryset.filter(
            date_joined__gte=today
        ).count()
        week_count = self.queryset.filter(
            date_joined__gte=week_start
        ).count()
        month_count = self.queryset.filter(
            date_joined__gte=month_start
        ).count()

        data = {
            'today': today_count,
            'this_week': week_count,
            'this_month': month_count,
        }

        return Response(data)
