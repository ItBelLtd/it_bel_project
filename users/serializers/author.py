from rest_framework import serializers
from ..models.author import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["author_id", "author_name", "name",
                  "surname", "age", "email", "date_joined"]