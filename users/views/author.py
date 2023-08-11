from mixins.author import AuthorMixin
from rest_framework import filters, viewsets

from ..models.author import Author
from ..serializers.author import AuthorSerializer
from users.permission import AuthorOwnerOrReadOnly


class AuthorViewSet(
    viewsets.ModelViewSet,
    AuthorMixin,
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AuthorOwnerOrReadOnly, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['surname', 'name']

    def perform_create(self, serializer: AuthorSerializer):
        return serializer.save(
            email=self.request.user.email,
            user=self.request.user
        )
