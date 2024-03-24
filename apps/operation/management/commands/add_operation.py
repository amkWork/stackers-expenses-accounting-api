from typing import Any

from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from ...models import Operation


class Command(BaseCommand):
    help = 'Add new operation'

    def add_arguments(
        self,
        parser: CommandParser,
    ) -> None:
        parser.add_argument('--name', '-N', type=str, required=True, help='Operation name')
        parser.add_argument('--value', '-V', type=float, required=True, help='Operation value')

    def handle(
        self,
        *args: Any,
        **options: Any,
    ) -> None:
        operation = Operation.objects.create(
            name=options['name'],
            value=options['value'],
        )

        self.stdout.write(f'Operation `{operation.name}` was successfully created!')
