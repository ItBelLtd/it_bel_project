from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from ..mixins.like import LikedMixin
from ..models.comment import Comment
from ..models.news import News
from ..permissions.comment import AuthorOrReadOnlyComments
from ..serializers.comment import CommentSerializer


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
