from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from ..models.user import User
from ..models.author import Author
from users.serializers.author import AuthorSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    date_joined = serializers.CharField(read_only=True)
    author = AuthorSerializer(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "date_joined", "author", ]

    def validate_password(self, password):
        validate_password(password)
        return password

    def create(self, validated_data: dict):
        password = validated_data.pop('password')
        author_data = validated_data.pop('author', None)

        user: User = super().create(validated_data)

        try:
            user.set_password(password)
            user.save()

            if author_data is not None:
                Author.objects.create(user=user, **author_data)

            return user
        except serializers.ValidationError as exc:
            user.delete()
            raise exc


class UserListSerializer(serializers.ModelSerializer):
    date_joined = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'date_joined']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
