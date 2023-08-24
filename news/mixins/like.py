from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .. import services


class LikeMixin:

    @action(detail=True,
            methods=['POST'],
            permission_classes=[IsAuthenticated]
            )
    def like(self, request, pk=None, news_id=None):
        services.add_remove_like(obj=self.get_object(), user=request.user)
        return Response({'status': 'ok'})


class DislikeMixin:

    @action(detail=True,
            methods=['POST'],
            permission_classes=[IsAuthenticated]
            )
    def dislike(self, request, pk=None, news_id=None):
        services.add_remove_dislike(obj=self.get_object(), user=request.user)
        return Response({'status': 'ok'})
