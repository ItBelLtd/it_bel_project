from rest_framework import serializers
from ..models.news import News


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField()

    class Meta:
        model = News
        fields = ['news_id', 'title', 'author',
                  'description', 'content', 'added', 'is_moderated', ]
