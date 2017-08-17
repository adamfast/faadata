import os

from optparse import make_option

from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand, CommandError

from faadata.airspace.models import *


class NoShapeFileException(Exception):
    pass


def airspace_import(path=''):
    from django.contrib.gis.gdal import DataSource

    airspace_mapping = {
        'mpoly': 'POLYGON',

        'ident': u'IDENT',
        'name': u'NAME',
        'upper_desc': u'UPPER_DESC',
        'upper_val': u'UPPER_VAL',
        'upper_uom': u'UPPER_UOM',
        'upper_code': u'UPPER_CODE',
        'lower_desc': u'LOWER_DESC',
        'lower_val': u'LOWER_VAL',
        'lower_uom': u'LOWER_UOM',
        'lower_code': u'LOWER_CODE',
        'type_code': u'TYPE_CODE',
        'local_type': u'LOCAL_TYPE',
        'airspace_class': u'CLASS',
        'mil_code': u'MIL_CODE',
        'comm_name': u'COMM_NAME',
        'level': u'LEVEL',
        'sector': u'SECTOR',
        'onshore': u'ONSHORE',
        'exclusion': u'EXCLUSION',
        'wkhr_code': u'WKHR_CODE',
        'wkhr_remark': u'WKHR_RMK',
        # None: u'DST',  # no data currently
        # None: u'GMTOFFSET',  # no data currently
        # None: u'SHAPE_Leng',  # no data currently
        # None: u'SHAPE_Area',  # no data currently
    }
    if os.path.exists(path):
        # spelunk the source
        ds = DataSource(path)
        layer = ds[0]
        print('Fields: %s' % layer.fields)
        print('Geom Type: %s' % layer.geom_type)
        print('SRS: %s' % layer.srs)

        lm = LayerMapping(Airspace, path, airspace_mapping)
        lm.save(verbose=True)
    else:
        raise NoShapeFileException


class Command(BaseCommand):
    args = ''
    help = 'Load timezones from the shapefile into the database.'

    def add_arguments(self, parser):
        # the rest of FAAdata infers the path, but right now the containing folder changes with each 28 day subscription edition which would make for a brittle loader
        parser.add_argument('--path', default='', dest='path',
                            help='The path to the FADDS airspace shapefile (.shp)')
        parser.add_argument('--clear_airspace', default=False, dest='clear_airspace', action='store_true',
                            help='Clear all airspace before import')

    def handle(self, *args, **options):
        base_path = options['path']

        if options['clear_airspace']:
            print("Clearing all airspaces...")
            # Timezone.objects.all().delete()
            print('Done clearing all airspaces.')

        airspace_import(base_path)
