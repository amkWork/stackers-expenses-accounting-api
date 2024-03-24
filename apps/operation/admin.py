from django.contrib.admin import ModelAdmin, register

from .models import Operation


@register(Operation)
class OperationAdmin(ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('name', 'created_at',)
    search_fields = ('name',)
    ordering = ('-created_at',)
