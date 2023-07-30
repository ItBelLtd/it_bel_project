from rest_framework import serializers

from ..models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    added = serializers.ReadOnlyField()
    total_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ['comment_id', 'text', 'author', 'total_likes', 'added']
