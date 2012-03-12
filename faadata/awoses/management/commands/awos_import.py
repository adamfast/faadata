from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

from faadata.awoses.load import awos_import


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--faddspath', default='', dest='fadds',
            help='The directory where the FADDS data is stored.'),
    )
    help = ("Imports AWOSes from the FADDS data download.")

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You must turn settings.DEBUG off, or else this script will eat a very large amount of your RAM. Aborting import.')
        else:
            input_path = options['fadds']

            awos_import(open(input_path + 'AWOS.txt'))
