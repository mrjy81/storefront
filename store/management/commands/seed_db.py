from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        print('Populating the database...')
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'seed.sql')
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            """
            execute() will only execute a single SQL statement.
             If you try to execute more than one statement with it,
            it will raise a Warning.
            Use executescript() if you want to execute multiple SQL statements
            with one call.
            """
            cursor.executescript(sql)
