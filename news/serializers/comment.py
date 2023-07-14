from rest_framework import serializers
from ..models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    added = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['comment_id', 'text', 'author', 'added']
