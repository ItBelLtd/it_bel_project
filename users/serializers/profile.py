from rest_framework import serializers

from ..models.author import Author
from ..models.user import User
from .author import AuthorSerializer
from news.serializers.news import NewsSerializer


class ProfileSerializer(serializers.ModelSerializer):
    news = serializers.SerializerMethodField(read_only=True)
    as_author = serializers.SerializerMethodField(read_only=True)

    def get_news(self, user: User):
        if not user.author:
            return {}
        serializer = NewsSerializer(user.author.news, many=True)
        return serializer.data

    def get_as_author(self, user: User):
        author = Author.objects.filter(email=user.email).first()
        if not author:
            return None

        serializer = AuthorSerializer(author)
        return serializer.data

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'as_author', 'news']
