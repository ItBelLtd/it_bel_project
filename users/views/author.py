from mixins.author import AuthorMixin
from rest_framework import filters, mixins, viewsets

from ..models.author import Author
from ..serializers.author import AuthorSerializer
from users.permissions.author import AuthorOwnerOrReadOnly


# We remove the inherited CreateModelMixin
# and DestroyModelMixin from the ModelViewSet,
# since these are methods for the user
# Check rest_framework/viewsets.py
class AuthorViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    AuthorMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AuthorOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['surname', 'name']
