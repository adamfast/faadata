import datetime
import os
import pandas

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from faadata.aircraft.load import import_aircraftregistration, import_aircraftmanufacturercodes


class Command(BaseCommand):
    help = ("Create a Pandas DataFrame of the FAA Aircraft Registry")

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
                            help='The directory where the aircraft data is stored.')

    def handle(self, *args, **options):
        input_path = options['path']
        df = pandas.read_csv(os.path.join(input_path, 'MASTER.txt'), dtype={'TYPE AIRCRAFT': 'object'})
        engine_df = pandas.read_csv(os.path.join(input_path, 'ENGINE.txt'), dtype={'CODE': 'object'})
        model_df = pandas.read_csv(os.path.join(input_path, 'ACFTREF.txt'), dtype={'CODE': 'object'})

        combined_df = pandas.merge(df, engine_df, left_on='ENG MFR MDL', right_on='CODE', how='left', suffixes=('_master', '_engine'))
        combined_df = pandas.merge(combined_df, model_df, left_on='MFR MDL CODE', right_on='CODE', how='left', suffixes=('_master', '_acftref'))

        combined_df.to_parquet(
            '/Users/adam/Personal-Projects/adsb/adsb_tools/adsb/faa-aircraft-registry-direct.parquet',
        )
