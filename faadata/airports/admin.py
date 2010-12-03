from django.contrib.gis import admin
from faadata.airports.models import Airport

class AirportAdmin(admin.OSMGeoAdmin):
#class AirportAdmin(admin.ModelAdmin):
    list_display = ('location_identifier', 'facility_name', 'elevation_msl', 'status')
    search_fields = ('location_identifier', 'icao_identifier', 'facility_name')

admin.site.register(Airport, AirportAdmin)
