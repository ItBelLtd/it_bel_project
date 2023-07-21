from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from ..models.author import Author
from ..serializers.author import AuthorSerializer
from news.serializers.news import NewsSerializer
from users.permission import AuthorOwnerOrReadOnly


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AuthorOwnerOrReadOnly]

    def perform_create(self, serializer: AuthorSerializer):
        author = serializer.save(email=self.request.user.email)
        self.request.user.author = author
        self.request.user.save()
        return author

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
