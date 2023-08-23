from rest_framework import filters, mixins, viewsets

from ..mixins.author import AuthorMixin
from ..mixins.follow import FollowMixin
from ..models.author import Author
from ..serializers.author import AuthorSerializer
from users.permissions.author import AuthorOwnerOrReadOnly


class AuthorViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    AuthorMixin,
                    FollowMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AuthorOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['surname', 'name']
