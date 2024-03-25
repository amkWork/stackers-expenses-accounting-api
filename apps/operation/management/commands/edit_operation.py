from typing import Any

from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from ...models import Operation


class Command(BaseCommand):
    help = 'Edit operation by ID'

    def add_arguments(
        self,
        parser: CommandParser,
    ) -> None:
        parser.add_argument('--id', '-i', type=int, required=True, help='Operation ID')
        parser.add_argument('--category', '-c', type=int, required=False, help='Category ID')

    def handle(
        self,
        *args: Any,
        **options: Any,
    ) -> None:
        operation_fields: set[str] = {field.name for field in Operation._meta.fields}
        operation_fields.remove('id')

        Operation.objects.filter(
            id=options['id'],
        ).update(**{
            field_name: field_value
            for field_name, field_value in options.items()
            if field_name in operation_fields
        })

        self.stdout.write(f'Operation `{options["id"]}` was successfully updated!')
