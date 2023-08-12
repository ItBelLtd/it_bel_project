from rest_framework import serializers

from ..models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = Author
        fields = [
            "author_id", "name", "surname", "age", "date_joined"
        ]
