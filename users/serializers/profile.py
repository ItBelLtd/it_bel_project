from rest_framework import serializers
from news.serializers.news import NewsSerializer
from ..models.user import User
from ..models.author import Author
from .author import AuthorSerializer


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
