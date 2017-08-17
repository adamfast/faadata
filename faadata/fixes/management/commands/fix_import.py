from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

from faadata.fixes.load import natfix_import


class Command(BaseCommand):
    help = ("Imports Fixes from the FADDS data download.")

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
                            help='The directory where the FADDS data is stored.')

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You must turn settings.DEBUG off, or else this script will eat a very large amount of your RAM. Aborting import.')
        else:
            input_path = options['path']

            natfix_import(open(input_path + 'NATFIX.txt'))
