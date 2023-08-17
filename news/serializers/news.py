from rest_framework import serializers
from serializers.tag import TagSerializer

from ..models.news import News
from users.serializers.author import AuthorSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    added = serializers.ReadOnlyField()
    total_likes = serializers.IntegerField(read_only=True)
    tags = TagSerializer(read_only=False, many=True)

    class Meta:
        model = News
        fields = ['news_id', 'title', 'author',
                  'description', 'content', 'total_likes', 'added', 'tags', ]
