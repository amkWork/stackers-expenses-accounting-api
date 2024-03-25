from typing import Any

from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from ...models import Category


class Command(BaseCommand):
    help = 'Add new category'

    def add_arguments(
        self,
        parser: CommandParser,
    ) -> None:
        parser.add_argument('--name', '-N', type=str, required=True, help='Category name')

    def handle(
        self,
        *args: Any,
        **options: Any,
    ) -> None:
        category = Category.objects.create(
            name=options['name'],
        )

        self.stdout.write(f'Category `{category.name}` was successfully created!')
