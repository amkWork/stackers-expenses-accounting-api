from django.http import HttpRequest, JsonResponse

from .models import Goal


def get_all_goals(_: HttpRequest) -> JsonResponse:
    return JsonResponse({
        'goals': list(Goal.objects.all()),
    })
