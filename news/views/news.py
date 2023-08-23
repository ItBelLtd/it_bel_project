from rest_framework import filters, viewsets
from rest_framework.exceptions import ValidationError

from ..mixins.like import LikedMixin
from ..models.news import News
from ..permissions.news import AuthorOrReadOnlyNews
from ..serializers.news import NewsSerializer
from news.mixins.news import NewsMixin
from users.models.user import User


class NewsViewSet(NewsMixin, viewsets.ModelViewSet, LikedMixin):

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
