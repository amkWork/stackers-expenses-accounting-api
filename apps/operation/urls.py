from django.urls import path

from .views import OperationList


urlpatterns = [
    path('all/', view=OperationList.as_view()),
]
