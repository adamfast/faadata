#!/home/bin/python
# -*- coding: utf-8
from django.contrib.gis.geos import Point
from decimal import Decimal
from faadata.airports.models import *
from faddsdata.apt import parse_apt_line
from faddsdata.parse import convert_boolean, convert_month_year

def clean_chars(value):
    value = value.replace('\xb9', ' ')
    value = value.replace('\xf8', ' ')
    value = value.replace('\xab', ' ')
    value = value.replace('\xa8', ' ')
    value = value.replace('\xfb', ' ')
    value = value.replace('\xfc', ' ')
    return value

def airport_import(importfile):
    Remark.objects.all().delete() # there's no way to version them. Start with a clean slate each time.
    Attendance.objects.all().delete()

    for line in importfile:
        data = parse_apt_line(clean_chars(line))
        if data['record_type'] == 'ATT':
            try:
                attendance = Attendance.objects.create(airport=airport, sequence=data['attendace_schedule_sequence'], schedule=data['attendance_schedule'])
            except:
                print data

        elif data['record_type'] == 'RMK':
            try:
                remark = Remark.objects.create(airport=airport, element_name=data['element_name'], body=data['element_text'])
            except:
                print data

        elif data['record_type'] == 'APT':
            try:
                airport = Airport.objects.get(facility_site_number=data['facility_site_number'])
            except Airport.DoesNotExist:
                airport = Airport(facility_site_number=data['facility_site_number'])

            airport.location_identifier = data['location_identifier']
            airport.facility_name = data['facility_name']
            airport.ownership_type = data['ownership_type']
            airport.use_type = data['use_type']
            airport.owners_name = data['owners_name']
            airport.facility_manager_name = data['facility_manager_name']
            airport.point = Point((data['lon'], data['lat']))
            airport.elevation_msl = data['elevation_msl']
            airport.traffic_pattern_agl = getattr(data, 'traffic_pattern_agl', None)
            airport.activation_date = convert_month_year(data['activation_date'])
            airport.status = data['status_code']
            airport.control_tower = convert_boolean(data['control_tower'])
            if data['common_traffic_advisory_frequency']:
                airport.ctaf = Decimal(data['common_traffic_advisory_frequency'])
            airport.segmented_circle = convert_boolean(data['segmented_circle'])
            airport.beacon_color = data['beacon_color']
            airport.landing_fees = convert_boolean(data['landing_fees'])
            airport.medical_use = convert_boolean(data['medical_use'])
            airport.singles_based = getattr(data, 'singles_based', 0)
            airport.multis_based = getattr(data, 'multis_based', 0)
            airport.jets_based = getattr(data, 'jets_based', 0)
            airport.helicopters_based = getattr(data, 'helicopters_based', 0)
            airport.gliders_based = getattr(data, 'gliders_based', 0)
            airport.military_based = getattr(data, 'military_based', 0)
            airport.ultralights_based = getattr(data, 'ultralights_based', 0)
            airport.icao_identifier = data['icao_identifier']
            try:
                airport.save()
            except:
                print('Airport data fail for %s' % data['location_identifer'])


if __name__ == '__main__':
    path = '/Users/adam/Downloads/56DySubscription_November_18__2010_-_January_13__2011/'
    airport_import(open(path + 'APT.txt'))
