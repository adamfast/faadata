from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

from faadata.airports.load import airport_import


class Command(BaseCommand):
    help = ("Imports data from the FADDS data download.")

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
                            help='The directory where the FADDS data is stored.')

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You must turn settings.DEBUG off, or else this script will eat a very large amount of your RAM. Aborting import.')
        else:
            input_path = options['path']

            airport_import(open(input_path + 'APT.txt'), {'import_att': True, 'import_rmk': True, 'import_rwy': True, 'import_apt': True}) # , max_records=100)
