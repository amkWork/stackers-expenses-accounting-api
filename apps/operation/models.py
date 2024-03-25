from django.db.models import (
    SET_NULL,
    CharField,
    DateTimeField,
    FloatField,
    ForeignKey,
    Model,
    TextField,
)
from django.utils import timezone


class Category(Model):
    name = CharField(max_length=64, verbose_name='Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Operation(Model):
    name = TextField(verbose_name='Name')
    description = TextField(null=True, verbose_name='Description')
    value = FloatField(verbose_name='Amount of money')
    created_at = DateTimeField(default=timezone.now, verbose_name='Perform date & time')

    category = ForeignKey(
        Category,
        null=True,
        on_delete=SET_NULL,
        related_name='operations',
        verbose_name='Category',
    )

    class Meta:
        verbose_name = 'Operation'
        verbose_name_plural = 'Operations'

    def __str__(self) -> str:
        return self.name
