from enum import auto

from django.db.models import TextChoices


class GoalHolderType(TextChoices):
    saving_account = auto()
    deposit = auto()
