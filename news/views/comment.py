from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from ..models.comment import Comment
from ..models.news import News
from ..serializers.comment import CommentSerializer
from news.mixins import LikedMixin
from news.permissions.comment import AuthorOrReadOnlyComments


class CommentViewSet(LikedMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AuthorOrReadOnlyComments]

    def get_queryset(self):
        news = get_object_or_404(News, news_id=self.kwargs.get('news_id'))
        return news.comments.all()

    def perform_create(self, serializer: CommentSerializer):
        serializer.save(
            news=get_object_or_404(News, news_id=self.kwargs.get('news_id')),
            author=self.request.user
        )
