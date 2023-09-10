from rest_framework import serializers

from ..models.comment import Comment
from ..services import get_vote
from users.models.user import User
from users.serializers.users import UserListSerializer


class CommentSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField(read_only=True)
    added = serializers.SerializerMethodField()
    author = UserListSerializer(read_only=True)
    vote = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'comment_id', 'text', 'author', 'total_likes', 'added', 'vote'
        ]

    def get_vote(self, obj: Comment) -> int:
        user: User = self.context.get('request').user
        if not user.is_authenticated:
            return 0

        like = get_vote(obj, user)
        if not like:
            return 0

        return like.vote

    def get_added(self, obj: Comment) -> str:
        return obj.get_date()
