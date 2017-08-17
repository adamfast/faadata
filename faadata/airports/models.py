from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import LineString
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

AIRPORT_OWNERSHIP_TYPES = (
    ('PU', 'PUBLICLY OWNED'),
    ('PR', 'PRIVATELY OWNED'),
    ('MA', 'AIR FORCE OWNED'),
    ('MN', 'NAVY OWNED'),
    ('MR', 'ARMY OWNED'),
)

FACILITY_USE_TYPES = (
    ('PU', 'OPEN TO THE PUBLIC'),
    ('PR', 'PRIVATE'),
)

AIRPORT_STATUSES = (
    ('CI', 'CLOSED INDEFINITELY'),
    ('CP', 'CLOSED PERMANENTLY'),
    ('O', 'OPERATIONAL'),
)


class Airport(models.Model):
    facility_site_number = models.CharField(max_length=11, primary_key=True, unique=True)
    location_identifier = models.CharField(max_length=7, unique=True)
    facility_name = models.CharField(max_length=50)
    facility_type = models.CharField(max_length=16)
    associated_city = models.CharField(max_length=40, blank=True, default='')
    associated_state_post_office_code = models.CharField(max_length=2)
    associated_state_name = models.CharField(max_length=20, blank=True, default='')
    ownership_type = models.CharField(max_length=2, choices=AIRPORT_OWNERSHIP_TYPES)
    use_type = models.CharField(max_length=2, choices=FACILITY_USE_TYPES)
    owners_name = models.CharField(max_length=35)
    facility_manager_name = models.CharField(max_length=35)
    point = models.PointField(srid=4326)
    elevation_msl = models.DecimalField(max_digits=7, decimal_places=1)
    traffic_pattern_agl = models.IntegerField(null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=AIRPORT_STATUSES)
    control_tower = models.BooleanField(default=False)
    ctaf = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    segmented_circle = models.BooleanField(default=False)
    beacon_color = models.CharField(max_length=3)
    landing_fees = models.BooleanField(default=False)
    medical_use = models.BooleanField(default=False)
    singles_based = models.IntegerField(default=0)
    multis_based = models.IntegerField(default=0)
    jets_based = models.IntegerField(default=0)
    helicopters_based = models.IntegerField(default=0)
    gliders_based = models.IntegerField(default=0)
    military_based = models.IntegerField(default=0)
    ultralights_based = models.IntegerField(default=0)
    icao_identifier = models.CharField(max_length=7)
    commercial_services_operations = models.IntegerField(default=0)
    commuter_services_operations = models.IntegerField(default=0)
    air_taxi_operations = models.IntegerField(default=0)
    ga_local_operations = models.IntegerField(default=0)
    ga_itinerant_operations = models.IntegerField(default=0)
    military_operations = models.IntegerField(default=0)
    operations_ending_date = models.DateField(null=True, blank=True)

    objects = models.GeoManager()

    def get_absolute_url(self):
        return reverse('airport_detail', args=[self.location_identifier])

    def locator_point(self):
        return self.point

    def runway_types(self):
        runway_types = []
        runways = self.runway_set.filter(airport=self)
        for runway in runways:
            for surface in runway.surface_type_condition.split('-'):
                if len(surface) > 1:
                    runway_types.append(surface)

        return runway_types

    def runway_lengths(self):
        runway_lengths = []
        runways = self.runway_set.filter(airport=self)
        for runway in runways:
            runway_lengths.append(runway.runway_length)

        return runway_lengths

    def __unicode__(self):
        return self.facility_name

class Remark(models.Model):
    airport = models.ForeignKey(Airport)
    element_name = models.CharField(max_length=13)
    body = models.TextField()

    objects = models.GeoManager()

    def __unicode__(self):
        return u'%s for %s' % (self.element_name, self.airport)

class Attendance(models.Model):
    airport = models.ForeignKey(Airport)
    sequence = models.IntegerField()
    schedule = models.TextField()

    objects = models.GeoManager()

    def __unicode__(self):
        return u'%s for %s' % (self.sequence, self.airport)

class Runway(models.Model):
    airport = models.ForeignKey(Airport)
    runway_identification = models.CharField(max_length=7)
    runway_length = models.IntegerField(null=True, blank=True)
    runway_width = models.IntegerField(null=True, blank=True)
    surface_type_condition = models.CharField(max_length=14, null=True, blank=True)
    surface_treatment = models.CharField(max_length=8, null=True, blank=True)
    pavement_classification_number = models.CharField(max_length=14, null=True, blank=True)
    lights_edge_intensity = models.CharField(max_length=8, null=True, blank=True)
    base_end_point = models.PointField(srid=4326, null=True, blank=True)
    base_end_elevation_physical_runway_end = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    base_end_displaced_threshold_point = models.PointField(srid=4326, null=True, blank=True)
    base_end_elevation_displaced_threshold = models.IntegerField(null=True, blank=True)
    base_end_displaced_threshold_length_from_end = models.IntegerField(null=True, blank=True)
    base_end_visual_glide_slope_indicators = models.CharField(max_length=8, null=True, blank=True)
    base_end_runway_visual_range_equipment_locations = models.CharField(max_length=8, null=True, blank=True)
    base_end_runway_visual_range_equipment = models.BooleanField(default=False)
    reciprocal_end_point = models.PointField(srid=4326, null=True, blank=True)
    reciprocal_end_elevation_physical_runway_end = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    reciprocal_end_displaced_threshold_point = models.PointField(srid=4326, null=True, blank=True)
    reciprocal_end_elevation_displaced_threshold = models.IntegerField(null=True, blank=True)
    reciprocal_end_displaced_threshold_length_from_end = models.IntegerField(null=True, blank=True)
    reciprocal_end_visual_glide_slope_indicators = models.CharField(max_length=8, null=True, blank=True)
    reciprocal_end_runway_visual_range_equipment_locations = models.CharField(max_length=8, null=True, blank=True)
    reciprocal_end_runway_visual_range_equipment = models.BooleanField(default=False)

    objects = models.GeoManager()

    def locator_point(self):
        if self.base_end_point and self.reciprocal_end_point:
            ls = LineString(self.base_end_point, self.reciprocal_end_point)
            return ls.centroid
        return None

    def __unicode__(self):
        return 'Rwy %s at %s' % (self.runway_identification, self.airport)

# integrate with the django-locator app for easy geo lookups if it's installed
if 'locator.objects' in settings.INSTALLED_APPS:
    from locator.objects.models import create_locator_object
    models.signals.post_save.connect(create_locator_object, sender=Airport)
    models.signals.post_save.connect(create_locator_object, sender=Runway)
