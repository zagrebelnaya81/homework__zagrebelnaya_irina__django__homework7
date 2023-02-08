import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            help="Delete only auto generated contacts",
            action="store_true",
        )

    def handle(self, *args, **options):

        logger = logging.getLogger("django")

        queryset = Contacts.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        queryset_for_delete = queryset

        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")

        logger.info(f"Current amount of contacts after: {queryset.count()}")
