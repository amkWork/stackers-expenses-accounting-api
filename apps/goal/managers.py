from django.db import models
from typing_extensions import Self

from .enums import GoalHolderType


class GoalManager(models.Manager):
    def saving_accounts(self) -> Self:
        return self.filter(holder_type=GoalHolderType.saving_account)

    def deposits(self) -> Self:
        return self.filter(holder_type=GoalHolderType.deposit)
