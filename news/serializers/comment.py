from rest_framework import serializers

from ..models.comment import Comment
from users.serializers.users import UserListSerializer


class CommentSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField(read_only=True)
    added = serializers.SerializerMethodField()
    author = UserListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['comment_id', 'text', 'author', 'total_likes', 'added']

    def get_added(self, obj: Comment) -> str:
        return obj.get_date()
