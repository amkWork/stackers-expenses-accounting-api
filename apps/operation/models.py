from django.db import models


class Operation(models.Model):
    name = models.TextField(verbose_name='Name')
    description = models.TextField(null=True, verbose_name='Description')
    value = models.FloatField(verbose_name='Amount of money')
    created_at = models.DateTimeField(verbose_name='Perform date & time')

    class Meta:
        verbose_name = 'Operation'
        verbose_name_plural = 'Operations'

    def __str__(self) -> str:
        return self.name
