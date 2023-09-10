from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models.news import News
from ..models.tag import Tag
from ..services import get_vote
from users.models.user import User
from users.serializers.author import AuthorSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    cover = Base64ImageField(required=False)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    vote = serializers.SerializerMethodField(read_only=True)
    added = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = [
            'news_id',
            'title',
            'author',
            'cover',
            'content',
            'tags',
            'added',
            'total_likes',
            'total_dislikes',
            'sum_rating',
            'vote'
        ]

        read_only_fields = [
            'total_likes',
            'total_dislikes',
            'sum_rating',
        ]

    def get_vote(self, obj: News) -> int:
        user: User = self.context.get('request').user
        if not user.is_authenticated:
            return 0

        like = get_vote(obj, user)
        if not like:
            return 0

        return like.vote

    def get_added(self, obj: News) -> str:
        return obj.get_date()

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        news = News.objects.create(**validated_data)
        news.tags.set(tags)
        return news
