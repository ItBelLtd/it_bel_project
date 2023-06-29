from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.news import NewsViewSet


router = SimpleRouter()
router.register(
    'news',
    NewsViewSet
)


urlpatterns = [
    path('', include(router.urls))
]
