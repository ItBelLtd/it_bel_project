import random

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from ..models.author import Author
from ..models.user import User
from users.serializers.author import AuthorSerializer


class UserCreateCustomSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'user_id', "username", "email", "password", "date_joined",
            "author",
        ]

    def validate_password(self, password):
        validate_password(password)
        return password

    def create(self, validated_data: dict):
        if 'username' in validated_data:
            username = validated_data.pop('username')
        else:
            username = f'username{random.randint(1000000, 9999999)}'

        password = validated_data.pop('password')
        author_data = validated_data.pop('author', None)

        user = User.objects.create(
            username=username,
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
    date_joined = serializers.SerializerMethodField()

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
