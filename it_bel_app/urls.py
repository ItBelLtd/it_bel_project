from django.urls import path
from django.views.generic import RedirectView

from it_bel_app.api_views.api_home import HomeView

urlpatterns = [
    path('', RedirectView.as_view(url='/api/home/')),
    path('api/home/', HomeView.as_view(), name='home-list'),

]
