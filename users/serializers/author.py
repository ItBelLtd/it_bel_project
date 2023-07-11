from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    def validate(self, data: dict):
        email = data.get('email')
        author = Author.objects.filter(email=email).first()
        if author:
            raise ValidationError('You have already created an author')
        return super().validate(data)

    class Meta:
        model = Author
        fields = [
            "author_id", "name", "surname", "age", "email", "date_joined"
        ]
