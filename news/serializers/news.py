from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models.news import News
from users.serializers.author import AuthorSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    added = serializers.ReadOnlyField()
    total_likes = serializers.IntegerField(read_only=True)
    cover = Base64ImageField(required=False)

    class Meta:
        model = News
        fields = ['news_id', 'title', 'author', 'cover',
                  'description', 'content', 'total_likes', 'added', ]
