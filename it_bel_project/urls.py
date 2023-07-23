from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='IT BEL',
        default_version='1.0.0',
        description='IT BEL Documentation',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')),
    path('api/', include('users.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path(
        'api/docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
