from rest_framework import filters, viewsets
from rest_framework.exceptions import ValidationError

from ..models.news import News
from ..serializers.news import NewsSerializer
from news.mixins import LikedMixin
from news.permissions.news import AuthorOrReadOnlyNews
from users.models.user import User


class NewsViewSet(LikedMixin, viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AuthorOrReadOnlyNews]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer: NewsSerializer):
        user: User = self.request.user
        if not hasattr(user, 'author'):
            raise ValidationError({'detail': 'Only authors can create News'})
        return serializer.save(author=user.author)
