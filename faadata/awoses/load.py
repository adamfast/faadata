#!/home/bin/python
# -*- coding: utf-8
from django.contrib.gis.geos import Point
from decimal import *
from faadata.airports.models import *
from faadata.awoses.models import *
from faddsdata.awos import parse_awos_line
from faddsdata.parse import convert_boolean, convert_month_year, convert_date

def awos_import(importfile):
    for line in importfile:
        data = parse_awos_line(line)

        try:
            airport = Airport.objects.get(facility_site_number=data['landing_facility_site_number'])
        except Airport.DoesNotExist:
            airport = None

        try:
            awos = AWOS.objects.get(identifier=data['id'])
        except AWOS.DoesNotExist:
            awos = AWOS(identifier=data['id'])

        awos.sensor_type = data['sensor_type']
        awos.commissioned = convert_boolean(data['commissioning_status'])
        try:
            if data['frequency']:
                awos.frequency = Decimal(data['frequency'])
        except InvalidOperation:
            pass
        try:
            if data['second_frequency']:
                awos.second_frequency = Decimal(data['second_frequency'])
        except InvalidOperation:
            pass
        awos.telephone = data['telephone_number']
        awos.airport = airport
        awos.city = data['city']
        awos.state = data['state_post_office_code']
        awos.effective_date = convert_date(data['information_effective'])
        if data.get('lon') and data.get('lat'):
            awos.point = Point((data['lon'], data['lat']))
        awos.save()
