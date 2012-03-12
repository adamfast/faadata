from django.contrib import admin
from models import *

class AircraftRegistrationAdmin(admin.ModelAdmin):
    list_display = ('n_number', 'aircraft_mfr_model_code', 'engine_mfr_model_code', 'year_mfg', 'city', 'state', 'aircraft_type', )
    list_filter = ('type_registrant', 'aircraft_type', 'engine_type', 'status_code')
    search_fields = ('n_number',)

class AircraftManufacturerCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'manufacturer', 'model', 'number_of_engines', 'number_of_seats', 'cruising_speed')
    list_filter = ('aircraft_type', 'engine_type', 'category', 'builder_certification_code')
    search_fields = ('code', 'manufacturer', 'model')


admin.site.register(AircraftRegistration, AircraftRegistrationAdmin)
admin.site.register(AircraftManufacturerCode, AircraftManufacturerCodeAdmin)
