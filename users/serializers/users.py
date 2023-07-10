from rest_framework import serializers
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', "email", "date_joined"]
