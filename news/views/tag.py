from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from news.models.tag import Tag
from news.serializers.tag import TagSerializer
from rest_framework import mixins


class TagViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = None
