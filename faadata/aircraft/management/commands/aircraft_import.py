import datetime
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from faadata.aircraft.load import import_aircraftregistration, import_aircraftmanufacturercodes


class Command(BaseCommand):
    help = ("Imports data from the FAA aircraft data download.")

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
                            help='The directory where the aircraft data is stored.')

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You really should turn settings.DEBUG off, or else this script will eat a very large amount of your RAM.')
        else:
            input_path = options['path']

            start_time = datetime.datetime.now()
            import_aircraftregistration(input_path)
            import_aircraftmanufacturercodes(input_path)
            print('Took %s' % (datetime.datetime.now() - start_time))
