from django.utils.datastructures import SortedDict

APT_RECORDS = SortedDict()
APT_RECORDS['record_type'] = 3
APT_RECORDS['facility_site_number'] = 11
APT_RECORDS['facility_type'] = 13
APT_RECORDS['location_identifier'] = 4
APT_RECORDS['information_effective_date'] = 10
APT_RECORDS['faa_region_code'] = 3
APT_RECORDS['faa_district_office_code'] = 4
APT_RECORDS['associated_state_post_office_code'] = 2
APT_RECORDS['associated_state_name'] = 20
APT_RECORDS['county_name'] = 21
APT_RECORDS['county_state_post_office_code'] = 2
APT_RECORDS['associated_city'] = 40
APT_RECORDS['facility_name'] = 42
APT_RECORDS['ownership_type'] = 2
APT_RECORDS['use_type'] = 2
APT_RECORDS['owners_name'] = 35
APT_RECORDS['owners_address'] = 72
APT_RECORDS['owners_city_state_zip'] = 45
APT_RECORDS['owners_phone_number'] = 16
APT_RECORDS['facility_manager_name'] = 35
APT_RECORDS['facility_manager_address'] = 72
APT_RECORDS['facility_manager_city_state_zip'] = 45
APT_RECORDS['facility_manager_phone_number'] = 16
APT_RECORDS['point_latitude_formatted'] = 15
APT_RECORDS['point_latitude_seconds'] = 12
APT_RECORDS['point_longitude_formatted'] = 15
APT_RECORDS['point_longitude_seconds'] = 12
APT_RECORDS['point_determination_method'] = 1
APT_RECORDS['elevation_msl'] = 5
APT_RECORDS['elevation_determination_method'] = 1
APT_RECORDS['magnetic_variation'] = 3
APT_RECORDS['magnetic_variation_epoch_year'] = 4
APT_RECORDS['traffic_pattern_agl'] = 4
APT_RECORDS['sectional'] = 30
APT_RECORDS['distance_to_central_business_district'] = 2
APT_RECORDS['direction_to_central_business_district'] = 3
APT_RECORDS['land_area_covered_acres'] = 5
APT_RECORDS['boundary_artcc_identifier'] = 4
APT_RECORDS['boundary_artcc_computer_identifier'] = 3
APT_RECORDS['boundary_artcc_name'] = 30
APT_RECORDS['responsible_artcc_identifier'] = 4
APT_RECORDS['responsible_artcc_computer_identifier'] = 3
APT_RECORDS['responsible_artcc_name'] = 30
APT_RECORDS['tie_in_fss_on_airport'] = 1
APT_RECORDS['tie_in_fss_identifier'] = 4
APT_RECORDS['tie_in_fss_name'] = 30
APT_RECORDS['local_phone_from_airport_to_fss_administrative'] = 16
APT_RECORDS['toll_free_from_airport_to_fss_briefing'] = 16
APT_RECORDS['alternate_fss_identifier'] = 4
APT_RECORDS['alternate_fss_name'] = 30
APT_RECORDS['toll_free_from_airport_to_alternate_fss_briefing'] = 16
APT_RECORDS['notam_issuing_fss_identifier'] = 4
APT_RECORDS['notam_d_available'] = 1
APT_RECORDS['activation_date'] = 7
APT_RECORDS['status_code'] = 2
APT_RECORDS['arff_certifcation_type_and_date'] = 15
APT_RECORDS['npias_federal_agreements_code'] = 7
APT_RECORDS['airport_airspace_analysis_determination'] = 13
APT_RECORDS['customs_airport_of_entry'] = 1
APT_RECORDS['customs_landing_rights'] = 1
APT_RECORDS['military_civil_joint_use'] = 1
APT_RECORDS['military_landing_rights'] = 1
APT_RECORDS['national_emergency_use_no_longer_maintained'] = 18
APT_RECORDS['military_departments_interest_for_emergencies_no_longer_maintained'] = 6
APT_RECORDS['airport_inspection_method'] = 2
APT_RECORDS['agency_group_performing_inspection'] = 1
APT_RECORDS['last_physical_inspection_date'] = 8
APT_RECORDS['last_information_date'] = 8
APT_RECORDS['available_fuels'] = 40
APT_RECORDS['airframe_repair'] = 5
APT_RECORDS['powerplant_repair'] = 5
APT_RECORDS['bottled_oxygen_available'] = 8
APT_RECORDS['bulk_oxygen_available'] = 8
APT_RECORDS['lighting_schedule'] = 9
APT_RECORDS['control_tower'] = 1
APT_RECORDS['unicom_frequencies'] = 42
APT_RECORDS['common_traffic_advisory_frequency'] = 7
APT_RECORDS['segmented_circle'] = 4
APT_RECORDS['beacon_color'] = 3
APT_RECORDS['landing_fees'] = 1
APT_RECORDS['medical_use'] = 1
APT_RECORDS['singles_based'] = 3
APT_RECORDS['multis_based'] = 3
APT_RECORDS['jets_based'] = 3
APT_RECORDS['helicopters_based'] = 3
APT_RECORDS['gliders_based'] = 3
APT_RECORDS['military_based'] = 3
APT_RECORDS['ultralights_based'] = 3
APT_RECORDS['commercial_services_operations'] = 6
APT_RECORDS['commuter_services_operations'] = 6
APT_RECORDS['air_taxi_operations'] = 6
APT_RECORDS['ga_local_operations'] = 6
APT_RECORDS['ga_itinerant_operations'] = 6
APT_RECORDS['military_operations'] = 6
APT_RECORDS['operations_ending_date'] = 10
APT_RECORDS['position_source'] = 16
APT_RECORDS['position_source_date'] = 10
APT_RECORDS['elevation_source'] = 16
APT_RECORDS['elevation_source_date'] = 10
APT_RECORDS['contract_fuel_available'] = 1
APT_RECORDS['transient_storage'] = 12
APT_RECORDS['other_services_available'] = 71
APT_RECORDS['wind_indicator'] = 3
APT_RECORDS['icao_identifier'] = 7

ATT_RECORDS = SortedDict()
ATT_RECORDS['record_type'] = 3
ATT_RECORDS['facility_site_number'] = 11
ATT_RECORDS['state_post_office_code'] = 2
ATT_RECORDS['attendace_schedule_sequence'] = 2
ATT_RECORDS['attendance_schedule'] = 108
ATT_RECORDS['record_filler'] = 1135

RWY_RECORDS = SortedDict()
RWY_RECORDS['record_type'] = 3
RWY_RECORDS['facility_site_number'] = 11
RWY_RECORDS['state_post_office_code'] = 2
RWY_RECORDS['runway_length'] = 5
RWY_RECORDS['runway_width'] = 4
RWY_RECORDS['surface_type_condition'] = 12
RWY_RECORDS['surface_treatment'] = 5
RWY_RECORDS['pavement_classification_number'] = 11
RWY_RECORDS['lights_edge_intensity'] = 5
RWY_RECORDS['base_end_identifier'] = 3
RWY_RECORDS['base_end_true_alignment'] = 3
RWY_RECORDS['base_end_ils_type'] = 10
RWY_RECORDS['base_end_righthand_traffic'] = 1
RWY_RECORDS['base_end_runway_markings_type'] = 5
RWY_RECORDS['base_end_runway_markings_condition'] = 1
RWY_RECORDS['base_end_aircraft_arresting_device'] = 6
RWY_RECORDS['base_end_latitude_physical_runway_end_formatted'] = 15
RWY_RECORDS['base_end_latitude_physical_runway_end_seconds'] = 12
RWY_RECORDS['base_end_longitude_physical_runway_end_formatted'] = 15
RWY_RECORDS['base_end_longitude_physical_runway_end_seconds'] = 12
RWY_RECORDS['base_end_elevation_physical_runway_end'] = 7
RWY_RECORDS['base_end_threshold_crossing_height_agl'] = 3
RWY_RECORDS['base_end_visual_glide_path_angle_degrees'] = 4
RWY_RECORDS['base_end_latitude_displaced_threshold_formatted'] = 15
RWY_RECORDS['base_end_latitude_displaced_threshold_seconds'] = 12
RWY_RECORDS['base_end_longitude_displaced_threshold_formatted'] = 15
RWY_RECORDS['base_end_longitude_displaced_threshold_seconds'] = 12
RWY_RECORDS['base_end_elevation_displaced_threshold'] = 7
RWY_RECORDS['base_end_displaced_threshold_length_from_end'] = 4
RWY_RECORDS['base_end_elevation_touchdown_zone'] = 7
RWY_RECORDS['base_end_visual_glide_slope_indicators'] = 5
RWY_RECORDS['base_end_runway_visual_range_equipment_locations'] = 3
RWY_RECORDS['base_end_runway_visual_range_equipment'] = 1
RWY_RECORDS['base_end_approach_light_system'] = 8
RWY_RECORDS['base_end_runway_end_identifer_lights'] = 1
RWY_RECORDS['base_end_runway_centerline_lights'] = 1
RWY_RECORDS['base_end_runway_end_touchdown_lights'] = 1
RWY_RECORDS['base_end_controlling_object_description'] = 11
RWY_RECORDS['base_end_controlling_object_marked_lighted'] = 4
RWY_RECORDS['base_end_runway_category'] = 5
RWY_RECORDS['base_end_controlling_object_clearance_slope'] = 2
RWY_RECORDS['base_end_controlling_object_height_above_runway'] = 5
RWY_RECORDS['base_end_controlling_object_distance_runway_end'] = 5
RWY_RECORDS['base_end_controlling_object_centerline_offset'] = 7
RWY_RECORDS['reciprocal_end_identifer'] = 3
RWY_RECORDS['reciprocal_end_true_alignment'] = 3
RWY_RECORDS['reciprocal_end_ils_type'] = 10
RWY_RECORDS['reciprocal_end_righthand_traffic'] = 1
RWY_RECORDS['reciprocal_end_runway_markings'] = 5
RWY_RECORDS['reciprocal_end_runway_markings_condition'] = 1
RWY_RECORDS['reciprocal_end_aircraft_arresting_device'] = 6
RWY_RECORDS['reciprocal_end_latitude_physical_runway_end_formatted'] = 15
RWY_RECORDS['reciprocal_end_latitude_physical_runway_end_seconds'] = 12
RWY_RECORDS['reciprocal_end_longitude_physical_runway_end_formatted'] = 15
RWY_RECORDS['reciprocal_end_longitude_physical_runway_end_seconds'] = 12
RWY_RECORDS['reciprocal_end_elevation_physical_runway_end'] = 7
RWY_RECORDS['reciprocal_end_threshold_crossing_height_agl'] = 3
RWY_RECORDS['reciprocal_end_visual_glide_path_angle_degrees'] = 4
RWY_RECORDS['reciprocal_end_latitude_displaced_threshold_formatted'] = 15
RWY_RECORDS['reciprocal_end_latitude_displaced_threshold_seconds'] = 12
RWY_RECORDS['reciprocal_end_longitude_displaced_threshold_formatted'] = 15
RWY_RECORDS['reciprocal_end_longitude_displaced_threshold_seconds'] = 12
RWY_RECORDS['reciprocal_end_elevation_displaced_threshold'] = 7
RWY_RECORDS['reciprocal_end_displaced_threshold_length_from_end'] = 4
RWY_RECORDS['reciprocal_end_elevation_touchdown_zone'] = 7
RWY_RECORDS['reciprocal_end_visual_glide_slope_indicators'] = 5
RWY_RECORDS['reciprocal_end_runway_visual_range_equipment_locations'] = 3
RWY_RECORDS['reciprocal_end_runway_visual_range_equipment'] = 1
RWY_RECORDS['reciprocal_end_approach_light_system'] = 8
RWY_RECORDS['reciprocal_end_runway_end_identifer_lights'] = 1
RWY_RECORDS['reciprocal_end_runway_centerline_lights'] = 1
RWY_RECORDS['reciprocal_end_runway_end_touchdown_lights'] = 1
RWY_RECORDS['reciprocal_end_controlling_object_description'] = 11
RWY_RECORDS['reciprocal_end_controlling_object_marked_lighted'] = 4
RWY_RECORDS['reciprocal_end_runway_category'] = 5
RWY_RECORDS['reciprocal_end_controlling_object_clearance_slope'] = 2
RWY_RECORDS['reciprocal_end_controlling_object_height_above_runway'] = 5
RWY_RECORDS['reciprocal_end_controlling_object_distance_runway_end'] = 5
RWY_RECORDS['reciprocal_end_controlling_object_centerline_offset'] = 7
RWY_RECORDS['runway_length_source'] = 16
RWY_RECORDS['runway_length_source_date'] = 10
RWY_RECORDS['runway_weight_bearing_single_wheel'] = 6
RWY_RECORDS['runway_weight_bearing_dual_wheel'] = 6
RWY_RECORDS['runway_weight_bearing_two_dual_wheels'] = 6
RWY_RECORDS['runway_weight_bearing_two_dual_wheels_tandem'] = 6
RWY_RECORDS['base_end_runway_end_gradient'] = 5
RWY_RECORDS['base_end_runway_end_gradient_direction'] = 4
RWY_RECORDS['base_end_runway_end_position_source'] = 16
RWY_RECORDS['base_end_runway_end_position_source_date'] = 10
RWY_RECORDS['base_end_runway_end_elevation_source'] = 16
RWY_RECORDS['base_end_runway_end_elevation_source_date'] = 10
RWY_RECORDS['base_end_displaced_threshold_position_source'] = 16
RWY_RECORDS['base_end_displaced_threshold_position_source_date'] = 10
RWY_RECORDS['displaced_threshold_elevation_source'] = 16
RWY_RECORDS['displaced_threshold_elevation_source_date'] = 10
RWY_RECORDS['touchdown_zone_elevation_source'] = 16
RWY_RECORDS['touchdown_zone_elevation_source_date'] = 10
RWY_RECORDS['takeoff_run_available_feet'] = 5
RWY_RECORDS['takeoff distance_available_feet'] = 5
RWY_RECORDS['aclt_stop_distance_available_feet'] = 5
RWY_RECORDS['landing_distance_available_feet'] = 5
RWY_RECORDS['available_landing_distance_lahso_feet'] = 5
RWY_RECORDS['intersecting_runway_lahso_id'] = 7
RWY_RECORDS['intersecting_entity_lahso_description_if_not_runway'] = 40
RWY_RECORDS['latitude_lahso_point_formatted'] = 15
RWY_RECORDS['latitude_lahso_point_seconds'] = 12
RWY_RECORDS['longitude_lahso_point_formatted'] = 15
RWY_RECORDS['longitude_lahso_point_seconds'] = 12
RWY_RECORDS['lahso_point_source'] = 16
RWY_RECORDS['lahso_point_source_date'] = 10
RWY_RECORDS['record_filler'] = 108

RMK_RECORDS = SortedDict()
RMK_RECORDS['record_type'] = 3
RMK_RECORDS['facility_site_number'] = 11
RMK_RECORDS['state_post_office_code'] = 2
RMK_RECORDS['element_name'] = 11
RMK_RECORDS['element_text'] = 700
RMK_RECORDS['record_filler'] = 534


def build_list_of_lengths(definition):
    """Take a SortedDict and iterate over it, building a list of field lengths."""
    lengths = []
    for key in definition:
        lengths.append(definition[key])
    return lengths

def calculate_lengths(fields):
    count = 0
    out = []
    for i in fields:
        end = 0
        for x in range(0, count):
            end += fields[x]
        if end != 0:
            out.append(end)
        count += 1
    return out

# calculate cumulative length from the list of lengths
APT_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(APT_RECORDS))
ATT_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(ATT_RECORDS))
RWY_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(RWY_RECORDS))
RMK_RECORD_LENGTHS = calculate_lengths(build_list_of_lengths(RMK_RECORDS))

# borrowed from http://code.activestate.com/recipes/65224/
def split_at(theline, cuts, lastfield=True):
    pieces = [ theline[i:j] for i, j in zip([0]+cuts, cuts) ]
    if lastfield:
        pieces.append(theline[cuts[-1]:])
    return pieces

def correlate(data, definition):
    combined = {}
    count = 0
    for key in definition.keys():
        combined[key] = data[count]
        count += 1
    return combined

if __name__ == '__main__':
    path = '/Users/afast/Downloads/56DySubscription_November_18__2010_-_January_13__2011/'
    raw = open(path + 'APT.txt')

    for line in raw:
        if line[:3] == 'APT':
            val = correlate(split_at(line, APT_RECORD_LENGTHS), APT_RECORDS)
        elif line[:3] == 'ATT':
            val = correlate(split_at(line, ATT_RECORD_LENGTHS), ATT_RECORDS)
        elif line[:3] == 'RWY':
            val = correlate(split_at(line, RWY_RECORD_LENGTHS), RWY_RECORDS)
        elif line[:3] == 'RMK':
            val = correlate(split_at(line, RMK_RECORD_LENGTHS), RMK_RECORDS)
        import pdb; pdb.set_trace()