from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from .models.author import Author
from .serializers.profile import ProfileSerializer
from news.serializers.news import NewsSerializer
from users.permission import IsModerator, UserOwnerOrReadOnly


class AuthorMixin:
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


class UserMixin:
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
