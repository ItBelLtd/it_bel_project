from django.http import HttpRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.user import User
from ..serializers.profile import ProfileSerializer
from ..serializers.users import UserSerializer
from users.permission import UserOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserOwnerOrReadOnly]

    @action(
        methods=['GET'],
        url_path='profile',
        detail=False,
        # permission_classes=[AuthorOrReadOnly, ]
    )
    def profile(self, request: HttpRequest):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
