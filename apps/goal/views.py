from django.http import HttpRequest, JsonResponse

from .models import Goal


def get_all_goals(_: HttpRequest) -> JsonResponse:
    goals = Goal.objects.all()

    return JsonResponse({
        'goals': list(goals.values()),
    })
