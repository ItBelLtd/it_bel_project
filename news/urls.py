from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views.comment import CommentViewSet
from .views.news import NewsViewSet
from .views.tag import TagViewSet

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
router.register(
    'tags',
    TagViewSet,
    basename='tags',
)


urlpatterns = [
    path('', include(router.urls))
]
