from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .filters import OperationFilterSet
from .models import Operation
from .serializers import OperationSerializer


class OperationList(ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_class = OperationFilterSet
    search_fields = ('name',)
