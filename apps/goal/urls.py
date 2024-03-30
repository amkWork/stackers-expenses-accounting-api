from django.urls import path

from .views import GoalList


urlpatterns = [
    path('all/', view=GoalList.as_view(), name='goal-list'),
]
