from random import randint
from string import ascii_letters

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from ..models.author import Author
from ..models.user import User
from users.serializers.author import AuthorSerializer


class UserCreateCustomSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    password = serializers.CharField(write_only=True)
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            'user_id', "username", "email", "password", "date_joined",
            "author",
        ]

    def validate_password(self, password):
        validate_password(password)
        return password

    def validate_username(self, username):
        valid_characters = ascii_letters + "1234567890-=*/{}[].,<>&^%$#@!*()_~"
        if all(map(
                lambda c: c in valid_characters,
                username
        )):
            return username
        return ValidationError("username cannot contain non-Latin characters")

    def create(self, validated_data: dict):
        if 'username' not in validated_data:
            validated_data['username'] = f'username{randint(1000000, 9999999)}'

        password = validated_data.pop('password')
        author_data = validated_data.pop('author', None)

        user = User.objects.create(
            **validated_data
        )

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
    as_author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'date_joined', 'as_author']

    def get_as_author(self, user: User) -> AuthorSerializer:
        author = Author.objects.filter(user=user).first()
        if not author:
            return None

        serializer = AuthorSerializer(author)
        return serializer.data

    def get_date_joined(self, obj: Author) -> str:
        return obj.get_date()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
