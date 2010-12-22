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

def airport_import(importfile, config={'import_att': True, 'import_rmk': True, 'import_rwy': True, 'import_apt': True}, max_records=10000000):
    if config['import_att']:
        Attendance.objects.all().delete()
    if config['import_rmk']:
        Remark.objects.all().delete() # there's no way to version them. Start with a clean slate each time.

    count = 0
    for line in importfile:
        data = parse_apt_line(clean_chars(line))

        try:
            airport = Airport.objects.get(facility_site_number=data['facility_site_number'])
        except Airport.DoesNotExist:
            airport = Airport(facility_site_number=data['facility_site_number'])

        if data['record_type'] == 'ATT' and config['import_att']:
            try:
                attendance = Attendance.objects.create(airport=airport, sequence=data['attendace_schedule_sequence'], schedule=data['attendance_schedule'])
            except:
                print data

        elif data['record_type'] == 'RMK' and config['import_rmk']:
            try:
                remark = Remark.objects.create(airport=airport, element_name=data['element_name'], body=data['element_text'])
            except:
                print data

        elif data['record_type'] == 'RWY' and config['import_rwy']:
            try:
                runway = Runway.objects.get(airport=airport, runway_identification=data['runway_identification'])
            except Runway.DoesNotExist:
                runway = Runway(airport=airport, runway_identification=data['runway_identification'])

            runway.runway_length = data['runway_length']
            runway.runway_width = data['runway_width']
            runway.surface_type_condition = data['surface_type_condition']
            runway.surface_treatment = data['surface_treatment']
            runway.pavement_classification_number = data['pavement_classification_number']
            runway.lights_edge_intensity = data['lights_edge_intensity']
            if getattr(data, 'base_end_lon', False) and getattr(data, 'base_end_lat', False):
                runway.base_end_point = Point((data['base_end_lon'], data['base_end_lat']))
            if data['base_end_elevation_physical_runway_end']:
                runway.base_end_elevation_physical_runway_end = Decimal(data['base_end_elevation_physical_runway_end'])
            if getattr(data, 'base_end_displaced_threshold_lon', False) and getattr(data, 'base_end_displaced_threshold_lat', False):
                runway.base_end_displaced_threshold_point = Point((data['base_end_displaced_threshold_lon'], data['base_end_displaced_threshold_lat']))
            if data['base_end_elevation_displaced_threshold']:
                runway.base_end_elevation_displaced_threshold = Decimal(data['base_end_elevation_displaced_threshold'])
            if data['base_end_displaced_threshold_length_from_end']:
                runway.base_end_displaced_threshold_length_from_end = data['base_end_displaced_threshold_length_from_end']
            runway.base_end_visual_glide_slope_indicators = data['base_end_visual_glide_slope_indicators']
            runway.base_end_runway_visual_range_equipment_locations = data['base_end_runway_visual_range_equipment_locations']
            runway.base_end_runway_visual_range_equipment = convert_boolean(data['base_end_runway_visual_range_equipment'])
            if getattr(data, 'reciprocal_end_lon', False) and getattr(data, 'reciprocal_end_lat', False):
                runway.reciprocal_end_point = Point((data['reciprocal_end_lon'], data['reciprocal_end_lat']))
            if data['reciprocal_end_elevation_physical_runway_end']:
                runway.reciprocal_end_elevation_physical_runway_end = Decimal(data['reciprocal_end_elevation_physical_runway_end'])
            if getattr(data, 'reciprocal_end_displaced_threshold_lon', False) and getattr(data, 'reciprocal_end_displaced_threshold_lat', False):
                runway.reciprocal_end_displaced_threshold_point = Point((data['reciprocal_end_displaced_threshold_lon'], data['reciprocal_end_displaced_threshold_lat']))
            if data['reciprocal_end_elevation_displaced_threshold']:
                runway.reciprocal_end_elevation_displaced_threshold = Decimal(data['reciprocal_end_elevation_displaced_threshold'])
            if data['reciprocal_end_displaced_threshold_length_from_end']:
                runway.reciprocal_end_displaced_threshold_length_from_end = data['reciprocal_end_displaced_threshold_length_from_end']
            runway.reciprocal_end_visual_glide_slope_indicators = data['reciprocal_end_visual_glide_slope_indicators']
            runway.reciprocal_end_runway_visual_range_equipment_locations = data['reciprocal_end_runway_visual_range_equipment_locations']
            runway.reciprocal_end_runway_visual_range_equipment = convert_boolean(data['reciprocal_end_runway_visual_range_equipment'])
            runway.save()

        elif data['record_type'] == 'APT' and config['import_apt']:
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
                print('Airport data fail for %s' % data['location_identifier'])

        count += 1
        if count > max_records:
            exit()

if __name__ == '__main__':
    path = '/Users/adam/Downloads/56DySubscription_January_13__2011_-_March_10__2011/'
    airport_import(open(path + 'APT.txt'), {'import_att': True, 'import_rmk': True, 'import_rwy': True, 'import_apt': True}) # , max_records=100)
