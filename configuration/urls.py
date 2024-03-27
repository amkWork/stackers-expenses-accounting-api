from django.contrib import admin
from django.urls import include, path
from drf_yasg.openapi import Info
from drf_yasg.views import get_schema_view


swagger_view = get_schema_view(
    info=Info(
        title='API documentation',
        default_version='0.0.1',
    ),
)


urlpatterns = [
    path('admin/', view=admin.site.urls),
    path('swagger/', view=swagger_view.with_ui('swagger', cache_timeout=0)),

    path('goal/', view=include('apps.goal.urls')),
    path('operation/', view=include('apps.operation.urls')),
]
