from datetime import date

from django.db import models

from . import enums, managers


class Goal(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    holder_type = models.CharField(
        choices=enums.GoalHolderType.choices,
        default=enums.GoalHolderType.saving_account,
        max_length=32,
        verbose_name='Holder type',
    )
    start_date = models.DateField(default=date.today, verbose_name='Start date')
    finish_date = models.DateField(null=True, verbose_name='Finish date')
    value = models.FloatField(verbose_name='Amount of money')

    objects = managers.GoalManager()

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'
