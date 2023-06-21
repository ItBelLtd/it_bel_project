from django.urls import path

from it_bel_app.api_views.api_home import HomeView

urlpatterns = [
    path('api/home/', HomeView.as_view(), name='home-view'),
]
