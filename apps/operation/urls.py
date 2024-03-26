from django.urls import path

from .views import get_all_operations


urlpatterns = [
    path('all/', view=get_all_operations),
]
