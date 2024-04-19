from django.core.management import BaseCommand

from mailing.services import my_job


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        my_job()
