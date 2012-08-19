import datetime

from faadata.aircraft.models import *
from tigerline.models import Zipcode


if __name__ == '__main__':
    print('Before:')
    print('%s aircraft have no point information' % AircraftRegistration.objects.filter(point__isnull=True).count())
    print('%s aircraft have point information' % AircraftRegistration.objects.filter(point__isnull=False).count())

    for aircraft in AircraftRegistration.objects.filter(point__isnull=True):
        try:
            aircraft.point = Zipcode.objects.get(code=aircraft.zip_code[:5]).mpoly.centroid
            aircraft.geocode_type = 'zi'
            aircraft.geocode_date = datetime.datetime.now()
            aircraft.save()
        except Zipcode.DoesNotExist:
            pass

    print('After:')
    print('%s aircraft have no point information' % AircraftRegistration.objects.filter(point__isnull=True).count())
    print('%s aircraft have point information' % AircraftRegistration.objects.filter(point__isnull=False).count())
