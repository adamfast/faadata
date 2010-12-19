from django.contrib.gis import admin
from faadata.airports.models import *

class AirportAdmin(admin.OSMGeoAdmin):
#class AirportAdmin(admin.ModelAdmin):
    list_display = ('location_identifier', 'facility_name', 'elevation_msl', 'status')
    search_fields = ('location_identifier', 'icao_identifier', 'facility_name', 'facility_site_number')

class RemarkAdmin(admin.ModelAdmin):
    list_display = ('airport', 'element_name')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('airport', 'sequence')

class RunwayAdmin(admin.OSMGeoAdmin):
    list_display = ('airport', 'runway_identification', 'runway_length', 'runway_width', 'surface_type_condition', 'surface_treatment')
    search_fields = ('airport__location_identifier', )

admin.site.register(Airport, AirportAdmin)
admin.site.register(Remark, RemarkAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Runway, RunwayAdmin)
