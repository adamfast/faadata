from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

class Airport(models.Model):
    facility_site_number = models.CharField(max_length=11, primary_key=True, unique=True)
    location_identifier = models.CharField(max_length=4)
    facility_name = models.CharField(max_length=42)
    ownership_type = models.CharField(max_length=2)
    use_type = models.CharField(max_length=2)
    owners_name = models.CharField(max_length=35)
    facility_manager_name = models.CharField(max_length=35)
    point = models.PointField(srid=4326)
    elevation_msl = models.IntegerField()
    traffic_pattern_agl = models.IntegerField(null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=2)
    control_tower = models.BooleanField()
    ctaf = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    segmented_circle = models.BooleanField()
    beacon_color = models.CharField(max_length=3)
    landing_fees = models.BooleanField()
    medical_use = models.BooleanField()
    singles_based = models.IntegerField()
    multis_based = models.IntegerField()
    jets_based = models.IntegerField()
    helicopters_based = models.IntegerField()
    gliders_based = models.IntegerField()
    military_based = models.IntegerField()
    ultralights_based = models.IntegerField()
    icao_identifier = models.CharField(max_length=7)

    def get_absolute_url(self):
        return reverse('airport_detail', args=[self.location_identifier])

    def __unicode__(self):
        return self.facility_name

class Remark(models.Model):
    airport = models.ForeignKey(Airport)
    element_name = models.CharField(max_length=11)
    body = models.TextField()

    def __unicode__(self):
        return u'%s for %s' % (self.element_name, self.airport)

class Attendance(models.Model):
    airport = models.ForeignKey(Airport)
    sequence = models.IntegerField()
    schedule = models.TextField()

    def __unicode__(self):
        return u'%s for %s' % (self.sequence, self.airport)

class Runway(models.Model):
    airport = models.ForeignKey(Airport)
    runway_identification = models.CharField(max_length='7')
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

    def __unicode__(self):
        return 'Rwy %s at %s' % (self.runway_identification, self.airport)
