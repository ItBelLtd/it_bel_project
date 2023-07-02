from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.news import NewsViewSet
from .views.comment import CommentViewSet


router = SimpleRouter()
router.register(
    'news',
    NewsViewSet,
)
router.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentViewSet,
)


urlpatterns = [
    path('', include(router.urls))
]
