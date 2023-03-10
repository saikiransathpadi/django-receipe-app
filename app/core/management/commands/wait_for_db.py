"""
Django command to wait for db connection to be available
"""

import time
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db """

    def handle(self, *args, **kwargs):
        """Entry point for command"""
        self.stdout.write('waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable waiting for 1 sec...")
                time.sleep(1)
        self.stdout.write("Datebase is up....")
