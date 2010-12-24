from django.contrib.gis import admin
from faadata.awoses.models import AWOS

class AWOSAdmin(admin.OSMGeoAdmin):
    list_display = ('identifier', 'sensor_type', 'commissioned')
    list_filter = ('sensor_type', 'commissioned')
    search_fields = ('identifier',)
    raw_id_fields = ('airport',)

admin.site.register(AWOS, AWOSAdmin)
