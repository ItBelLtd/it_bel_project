from rest_framework import viewsets
from ..models.author import Author
from ..serializers.author import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer: AuthorSerializer):
        author = serializer.save(email=self.request.user.email)
        self.request.user.author = author
        self.request.user.save()
        return author
