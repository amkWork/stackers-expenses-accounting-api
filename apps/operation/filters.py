from django_filters import FilterSet, NumberFilter

from .models import Operation


class OperationFilterSet(FilterSet):
    category = NumberFilter(lookup_expr='exact')

    class Meta:
        model = Operation
        fields = ('category',)
