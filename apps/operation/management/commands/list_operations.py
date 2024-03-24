from typing import Any

from django.core.management.base import BaseCommand

from ...models import Operation


class Command(BaseCommand):
    help = 'List all operations'

    def handle(
        self,
        *args: Any,
        **options: Any,
    ) -> None:
        operations = Operation.objects.all()

        for operation in operations:
            self.stdout.write(
                f'{operation.value:-12.2f} - {operation.name}',
                self.style.SUCCESS if operation.value > 0 else self.style.ERROR,
            )
