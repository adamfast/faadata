from django.contrib.gis import admin
from faadata.airports.models import *

@admin.register(Airport)
class AirportAdmin(admin.OSMGeoAdmin):
#class AirportAdmin(admin.ModelAdmin):
    list_display = ('location_identifier', 'facility_name', 'elevation_msl', 'status')
    list_filter = ('facility_type', 'control_tower')
    search_fields = ('location_identifier', 'icao_identifier', 'facility_name', 'facility_site_number')

@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    list_display = ('airport', 'element_name')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('airport', 'sequence')

@admin.register(Runway)
class RunwayAdmin(admin.OSMGeoAdmin):
    list_display = ('airport', 'runway_identification', 'runway_length', 'runway_width', 'surface_type_condition', 'surface_treatment')
    search_fields = ('airport__location_identifier', )

