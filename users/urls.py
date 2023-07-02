from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.author import AuthorViewSet

router = SimpleRouter()
router.register(
    'authors',
    AuthorViewSet
)

urlpatterns = [
    path('', include(router.urls))
]