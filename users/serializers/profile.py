from rest_framework import serializers
from ..models.user import User
from ..models.author import Author
from .author import AuthorSerializer


class ProfileSerializer(serializers.ModelSerializer):
    as_author = serializers.SerializerMethodField(read_only=True)

    def get_as_author(self, user: User):
        author = Author.objects.filter(email=user.email).first()
        if not author:
            return None

        serializer = AuthorSerializer(author)
        return serializer.data

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'as_author']
