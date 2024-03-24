from django.db.models import DateTimeField, FloatField, Model, TextField
from django.utils import timezone


class Operation(Model):
    name = TextField(verbose_name='Name')
    description = TextField(null=True, verbose_name='Description')
    value = FloatField(verbose_name='Amount of money')
    created_at = DateTimeField(default=timezone.now, verbose_name='Perform date & time')

    class Meta:
        verbose_name = 'Operation'
        verbose_name_plural = 'Operations'

    def __str__(self) -> str:
        return self.name
