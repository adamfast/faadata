from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from faadata.airports.load import airport_import
from faadata.awoses.load import awos_import
from faadata.fixes.load import natfix_import

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--faddspath', default='', dest='fadds',
            help='The directory where the FADDS data is stored.'),
    )
    help = ("Imports data from the FADDS data download.")

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You really should turn settings.DEBUG off, or else this script will eat a very large amount of your RAM.')
        else:
            input_path = options['fadds']

            airport_import(open(input_path + 'APT.txt'), {'import_att': True, 'import_rmk': True, 'import_rwy': True, 'import_apt': True}) # , max_records=100)
            awos_import(open(input_path + 'AWOS.txt'))
            natfix_import(open(input_path + 'NATFIX.txt'))
