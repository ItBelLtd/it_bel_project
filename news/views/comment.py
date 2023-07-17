from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from news.permission import AuthorOrReadOnly

from ..models.comment import Comment
from ..models.news import News
from ..serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        news = get_object_or_404(News, news_id=self.kwargs.get('news_id'))
        return news.comments

    def perform_create(self, serializer: CommentSerializer):
        serializer.save(
            news=get_object_or_404(News, news_id=self.kwargs.get('news_id')),
            author=self.request.user
        )
