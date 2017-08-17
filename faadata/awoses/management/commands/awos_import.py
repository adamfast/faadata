from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

from faadata.awoses.load import awos_import


class Command(BaseCommand):
    help = ("Imports AWOSes from the FADDS data download.")

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
                            help='The directory where the aircraft data is stored.')

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You must turn settings.DEBUG off, or else this script will eat a very large amount of your RAM. Aborting import.')
        else:
            input_path = options['path']

            awos_import(open(input_path + 'AWOS.txt'))
