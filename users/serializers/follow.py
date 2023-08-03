from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models.follow import Follow


class FollowSerializer(serializers.ModelSerializer):
    def validate(self, data: dict):
        if data.get('author') == data.get('follower'):
            raise serializers.ValidationError(
                {'detail': 'You cannot subscribe on yourself'}
            )
        return super().validate(data)

    class Meta:
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['author', 'follower']
            )
        ]
        fields = [
            'author', 'follower'
        ]
