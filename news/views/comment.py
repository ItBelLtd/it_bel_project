from rest_framework import viewsets
from ..serializers.comment import CommentSerializer
from ..models.comment import Comment
from ..models.news import News
from django.shortcuts import get_object_or_404


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        news = get_object_or_404(News, news_id=self.kwargs.get('news_id'))
        return news.comments
