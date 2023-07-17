from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from news.permission import AuthorOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from ..models.news import News
from users.models.author import Author
from users.models.user import User
from ..serializers.news import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AuthorOrReadOnly]

    def perform_create(self, serializer: NewsSerializer):
        user: User = self.request.user
        if not user.author:
            raise ValidationError('Only authors can create News')
        return serializer.save(author=user.author)

    @action(
        methods=['GET', ],
        detail=False,
        url_path='moderate',
        # permission_classes=[IsAdminUser, ]
    )
    def moderate(self, request: HttpRequest):
        news = News.objects.filter(is_moderated=False)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    @action(
        methods=['POST', ],
        detail=True,
        url_path='approve',
        # permission_classes=[IsAdminUser, ]
    )
    def approve(self, request: HttpRequest, pk: int):
        news = get_object_or_404(News, news_id=pk)
        news.is_moderated = True
        news.save()
        serializer = NewsSerializer(news)
        return Response(serializer.data)
