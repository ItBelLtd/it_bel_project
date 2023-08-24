from django.urls import path

from .views.create import CustomTokenCreateView
from .views.destroy import CustomTokenDestroyView

urlpatterns = [
    path('login/', CustomTokenCreateView.as_view(), name='token_create'),
    path('logout/', CustomTokenDestroyView.as_view(), name='token_destroy')
]
