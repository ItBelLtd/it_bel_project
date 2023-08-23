from django.urls import path

from .views import CustomTokenCreateView

urlpatterns = [
    path('login/', CustomTokenCreateView.as_view(), name='token_create'),
]
