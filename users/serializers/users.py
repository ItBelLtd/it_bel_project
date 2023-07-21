from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from ..models.user import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    date_joined = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'date_joined', 'password']

    def validate_password(self, password):
        validate_password(password)
        return password

    def create(self, validated_data: dict):
        password = validated_data.pop('password')
        user: User = super().create(validated_data)
        try:
            user.set_password(password)
            user.save()
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
