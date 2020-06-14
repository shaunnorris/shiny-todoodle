import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.NOTICE('\nConnecting to db...')
            )
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING('db unavailable, waiting...')
                    )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('db available'))
