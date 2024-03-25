from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', view=admin.site.urls),

    path('goal/', view=include('apps.goal.urls')),
    path('operation/', view=include('apps.operation.urls')),
]
