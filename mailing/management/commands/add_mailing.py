from django.core.management import call_command
from django.core.management.base import BaseCommand

from mailing.models import Message, Recipient


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Message.objects.all().delete()
        Recipient.objects.all().delete()

        call_command("loaddata", "message_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
        call_command("loaddata", "recipient_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
