import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contacts
from apps.contacts.services.contacts_generate import contacts_generate


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            help="How many contacts do you want to generate?",
            type=int,
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        logger = logging.getLogger("django")

        queryset = Contacts.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        for contacts in contacts_generate(amount=amount):
            contacts.save()

        logger.info(f"Current amount of contacts after: {queryset.count()}")
