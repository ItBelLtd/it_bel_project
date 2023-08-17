from models.tag import Tag
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers.tag import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = None
