from rest_framework import serializers
from ..models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'text', 'owner_author', 'owner_user', 'added']
