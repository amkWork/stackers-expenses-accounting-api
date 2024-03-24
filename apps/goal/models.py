from datetime import date

from django.db.models import CharField, DateField, FloatField, Model, TextField

from .enums import GoalHolderType
from .managers import GoalManager


class Goal(Model):
    name = CharField(max_length=255, verbose_name='Name')
    description = TextField(verbose_name='Description')
    holder_type = CharField(
        choices=GoalHolderType.choices,
        default=GoalHolderType.saving_account,
        max_length=32,
        verbose_name='Holder type',
    )
    start_date = DateField(default=date.today, verbose_name='Start date')
    finish_date = DateField(null=True, verbose_name='Finish date')
    value = FloatField(verbose_name='Amount of money')

    objects = GoalManager()

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'
