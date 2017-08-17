import csv
import os
from decimal import Decimal

from django.contrib.gis.geos import Point
from django.core.cache import cache
from django.core.management.base import BaseCommand

from faadata.airports.models import Airport


class Command(BaseCommand):  # pragma: no cover
    help = ("Imports data from the OurAirports data download.")

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
                            help='The directory where the OurAirports data is stored.')

    def handle(self, *args, **options):
        ourairports_file = open(os.path.join(options['path'], 'airports.csv'), 'rU')
        ourairports_csv = csv.reader(ourairports_file, quoting=csv.QUOTE_MINIMAL, delimiter=',')

        for airport in ourairports_csv:
            print airport

            if airport[0] != 'id':
                airport_id = "oura-%s" % airport[0]
                try:
                    this_airport = Airport.objects.get(location_identifier=airport[1])
                except Airport.DoesNotExist:
                    this_airport = Airport(location_identifier=airport[1])

                if this_airport.facility_site_number != '' and not this_airport.facility_site_number.startswith('oura-'):
                    continue  # came in from FAA data, don't overwrite that

                if not this_airport.facility_site_number:
                    this_airport.facility_site_number = airport_id  # set if not set, but don't overwrite this if it's there, since it's the PK will cause a new record to be saved and that will conflict since location_identifier is enforced unique
                elif this_airport.facility_site_number != airport_id:  # it's changed
                    print("PK for %s has changed from %s to %s" % (this_airport.location_identifier, this_airport.facility_site_number, airport_id))
                this_airport.facility_type = airport[2]
                this_airport.facility_name = airport[3][:50]
                this_airport.associated_city = airport[10][:40]
                this_airport.associated_state_post_office_code = airport[9].replace('US-', '')[:2] if airport[9].startswith('US') else ''

                if len(airport[4]) > 0 and len(airport[5]) > 0:
                    this_airport.point = Point((Decimal(airport[5]), Decimal(airport[4])),)

                if len(airport[6]) > 0:
                    this_airport.elevation_msl = airport[6]
                else:
                    this_airport.elevation_msl = -1111

                this_airport.icao_identifier = airport[13]
                if len(airport[4]) > 0 and len(airport[5]) > 0:
                    this_airport.save()
                else:
                    print("No point was available for %s so it was skipped." % airport[1])


# [00] "id",
# [01] "ident",
# [02] "type",
# [03] "name",
# [04] "latitude_deg",
# [05] "longitude_deg",
# [06] "elevation_ft",
# [07] "continent",
# [08] "iso_country",
# [09] "iso_region",
# [10] "municipality",
# [11] "scheduled_service",
# [12] "gps_code",
# [13] "iata_code",
# [14] "local_code",
# [15] "home_link",
# [16] "wikipedia_link",
# [17] "keywords"
