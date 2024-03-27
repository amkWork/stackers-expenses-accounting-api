from rest_framework.generics import ListAPIView

from .models import Goal
from .serializers import GoalSerializer


class GoalList(ListAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
