import random
from datetime import timedelta

from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.utils import timezone
from models.news import News
from rest_framework.decorators import action
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from ..serializers.news import NewsSerializer
from users.permission import IsModerator


class NewsMixin:
    @action(
        methods=['GET', ],
        detail=False,
        url_path='popular',
    )
    def get_popular_news(self, request: HttpRequest):
        """
        Retrieve most popular news articles added in the last 7 days by
        filtering on the added field.

        Add a new field likes_total to each article using annotate() method.

        Order queryset by likes_total in ascending order using order_by().

        Select first 6 articles using slicing and randomize their order using
        random.shuffle().
        """
        date = timezone.now().date() - timedelta(days=7)
        news = News.objects.filter(
            added__gte=date
        ).annotate(
            likes_total=Count('likes')
        ).order_by(
            'likes_total'
        )[:6]
        random.shuffle(news)
        return Response(NewsSerializer(news, many=True).data)

    @action(
        methods=['GET', ],
        detail=False,
        url_path='moderate',
        permission_classes=[IsModerator, ]
    )
    def moderate(self, request: HttpRequest):
        news = News.objects.filter(is_moderated=False)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    @action(
        methods=['POST', ],
        detail=True,
        url_path='approve',
        permission_classes=[IsModerator, ]
    )
    def approve(self, request: HttpRequest, pk: int):
        news = get_object_or_404(News, news_id=pk)
        news.is_moderated = True
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data)
