from enum import auto

from django.db import models


class GoalHolderType(models.TextChoices):
    saving_account = auto()
    deposit = auto()
