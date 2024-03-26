from http import HTTPStatus

from django.db.models import F
from django.http import HttpRequest, JsonResponse

from .models import Operation


def get_all_operations(request: HttpRequest) -> JsonResponse:
    offset: str = request.GET.get('offset', '0')
    limit: str = request.GET.get('limit', '20')

    if not offset.isdigit() or not limit.isdigit():
        return JsonResponse(
            {'message': 'Pagination parameters are not valid numbers.'},
            status=HTTPStatus.BAD_REQUEST,
        )

    offset = int(offset)
    limit = int(limit)

    operations = Operation.objects.order_by('-created_at')

    if category_id := request.GET.get('category-id'):
        operations = operations.filter(category=category_id)

    operations = operations[offset:offset + limit]

    operations = operations.annotate(category_name=F('category__name'))

    return JsonResponse({
        'operations': list(operations.values()),
    })
