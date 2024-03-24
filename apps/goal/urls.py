from django.urls import path

from .views import get_all_goals


urlpatterns = [
    path('all', get_all_goals),
]
