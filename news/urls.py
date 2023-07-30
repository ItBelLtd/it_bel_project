from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views.comment import CommentViewSet
from .views.news import NewsViewSet

router = SimpleRouter()
router.register(
    'news',
    NewsViewSet,
    basename='news'
)
router.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('', include(router.urls))
]
