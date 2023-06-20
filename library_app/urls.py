from django.urls import path
from .views import LibraryHome

urlpatterns = [
    path("", LibraryHome.as_view())
]