from django.contrib.gis.db import models

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

    def __unicode__(self):
        return self.facility_name
