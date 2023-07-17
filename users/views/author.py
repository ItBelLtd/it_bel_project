from rest_framework import viewsets
from ..models.author import Author
from ..serializers.author import AuthorSerializer
from users.permission import AuthorOwnerOrReadOnly

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AuthorOwnerOrReadOnly]

    def perform_create(self, serializer: AuthorSerializer):
        author = serializer.save(email=self.request.user.email)
        self.request.user.author = author
        self.request.user.save()
        return author
