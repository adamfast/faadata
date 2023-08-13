from django.contrib.gis import admin
from faadata.fixes.models import *

@admin.register(Fix)
class FixAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'artcc', 'fix_type', 'state_post_office_code')
    list_filter = ('fix_type', 'artcc')
    search_fields = ('id',)

