from rest_framework import serializers

from ..models.news import News
from users.serializers.author import AuthorSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    added = serializers.ReadOnlyField()

    class Meta:
        model = News
        fields = ['news_id', 'title', 'author',
                  'description', 'content', 'added', ]
