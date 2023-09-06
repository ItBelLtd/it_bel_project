from rest_framework import serializers

from ..models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = [
            "author_id", "name", "surname", "age", "date_joined", 'bio'
        ]

    def get_date_joined(self, obj: Author) -> str:
        return obj.get_date()
