from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^django\.contrib\.gis\.db\.models\.fields\.PointField"])
except ImportError: # don't require South to be installed
    pass

TYPE_REGISTRANT_CHOICES = (
    (1, 'Individual'),
    (2, 'Partnership'),
    (3, 'Corporation'),
    (4, 'Co-Owned'),
    (5, 'Government'),
    (8, 'Non-Citizen Corporation'),
    (9, 'Non-Citizen Co-Owned'),
)

REGION_CHOICES = (
    (1, 'Eastern'),
    (2, 'Southwestern'),
    (3, 'Central'),
    (4, 'Western-Pacific'),
    (5, 'Alaskan'),
    (7, 'Southern'),
    (8, 'European'),
    ('C', 'Great Lakes'),
    ('E', 'New England'),
    ('S', 'Northwest Mountain'),
)

AIRWORTHINESS_CODE = (
    (1, 'Standard'),
    (2, 'Limited'),
    (3, 'Restricted'),
    (4, 'Experimental'),
    (5, 'Provisional'),
    (6, 'Multiple'),
    (7, 'Primary'),
    (8, 'Special Flight Permit'),
    (9, 'Light Sport'),
)

AIRCRAFT_TYPE = (
    (1, 'Glider'),
    (2, 'Balloon'),
    (3, 'Blimp/Dirigible'),
    (4, 'Fixed wing single engine'),
    (5, 'Fixed wing multi engine'),
    (6, 'Rotorcraft'),
    (7, 'Weight-shift-control'),
    (8, 'Powered Parachute'),
    (9, 'Gyroplane'),
)

ENGINE_TYPE = (
    (0, 'None'),
    (1, 'Reciprocating'),
    (2, 'Turbo-prop'),
    (3, 'Turbo-shaft'),
    (4, 'Turbo-jet'),
    (5, 'Turbo-fan'),
    (6, 'Ramjet'),
    (7, '2 Cycle'),
    (8, '4 Cycle'),
    (9, 'Unknown'),
)

AIRCRAFT_CATEGORY_CODES = (
    (1, 'Land'),
    (2, 'Sea'),
    (3, 'Amphibian'),
)

BUILDER_CERTIFICATION_CODES = (
    (0, 'Type Certificated'),
    (1, 'Not Type Certificated'),
    (2, 'Light Sport'),
)

AIRCRAFT_STATUS_OPTIONS = (
    # per ARData.pdf in the aircraft registration download
    ('A', 'The Triennial Aircraft Registration form was mailed and has not been returned by the Post Office'),
    ('D', 'Expired Dealer'),
    ('E', 'The Certificate of Aircraft Registration was revoked by enforcement action'),
    ('M', 'Aircraft registered to the manufacturer under their Dealer Certificate'),
    ('N', 'Non-citizen Corporations which have not returned their flight hour reports'),
    ('R', 'Registration pending'),
    ('S', 'Second Triennial Aircraft Registration Form has been mailed'),
    ('T', 'Valid Registration from a Trainee'),
    ('V', 'Valid Registration'),
    ('X', 'Enforcement Letter'),
    ('Z', 'Permanent Reserved'),
    ('1', 'Triennial Aircraft Registration form was returned by the Post Office as undeliverable'),
    ('2', 'N-Number Assigned - but has not yet been registered'),
    ('3', 'N-Number assigned as a Non Type Certificated aircraft - but has not yet been registered'),
    ('4', 'N-Number assigned as import - but has not yet been registered'),
    ('5', 'Reserved N-Number'),
    ('6', 'Administratively canceled'),
    ('7', 'Sale reported'),
    ('8', 'A second attempt has been made at mailing a Triennial Aircraft Registration form to the owner with no response'),
    ('9', 'Certificate of Registration has been revoked'),
    ('10', 'N-Number assigned, has not been registered and is pending cancellation'),
    ('11', 'N-Number assigned as a Non Type Certificated (Amateur) but has not been registered that is pending cancellation'),
    ('12', 'N-Number assigned as import but has not been registered that is pending cancellation'),
    ('13', 'Registration Expired'),
    ('14', 'First Notice for Re-Registration/Renewal'),
    ('15', 'Second Notice for Re-Registration/Renewal'),
    ('16', 'Registration Expired - Pending Cancellation'),
    ('17', 'Sale Reported - Pending Cancellation'),
    ('18', 'Sale Reported - Canceled'),
    ('19', 'Registration Pending - Pending Cancellation'),
    ('20', 'Registration Pending - Canceled'),
    ('21', 'Revoked - Pending Cancellation'),
    ('22', 'Revoked - Canceled'),
    ('23', 'Expired Dealer (Pending Cancellation)'),
    ('24', 'Third Notice for Re-Registration/Renewal'),
)


class AircraftManufacturerCode(models.Model):
    code = models.CharField(max_length=8, db_index=True)
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    aircraft_type = models.CharField(max_length=1, choices=AIRCRAFT_TYPE)
    engine_type = models.CharField(max_length=1, choices=ENGINE_TYPE)
    category = models.CharField(max_length=1, choices=AIRCRAFT_CATEGORY_CODES)
    builder_certification_code = models.CharField(max_length=1, choices=BUILDER_CERTIFICATION_CODES)
    number_of_engines = models.CharField(max_length=2)
    number_of_seats = models.CharField(max_length=3)
    aircraft_weight = models.CharField(max_length=7)
    cruising_speed = models.CharField(max_length=4)

    objects = models.GeoManager()

    def __unicode__(self):
        return u'%s %s' % (self.manufacturer, self.model)


class AircraftRegistration(models.Model):
    n_number = models.CharField(max_length=5, db_index=True)
    serial_number = models.CharField(max_length=30, null=True, blank=True)
    aircraft_mfr_model_code = models.CharField(max_length=7, null=True, blank=True)
    engine_mfr_model_code = models.CharField(max_length=5, null=True, blank=True)
    year_mfg = models.CharField(max_length=4, null=True, blank=True)
    type_registrant = models.IntegerField(choices=TYPE_REGISTRANT_CHOICES, null=True, blank=True)
    registrant_name = models.CharField(max_length=50, null=True, blank=True)
    street1 = models.CharField(max_length=33, null=True, blank=True)
    street2 = models.CharField(max_length=33, null=True, blank=True)
    city = models.CharField(max_length=18, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    region = models.CharField(max_length=1, choices=REGION_CHOICES, null=True, blank=True)
    county = models.CharField(max_length=3, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    last_activity_date = models.DateField(null=True, blank=True)
    certificate_issue_date = models.DateField(null=True, blank=True)
    airworthiness_classification_code = models.CharField(max_length=1, choices=AIRWORTHINESS_CODE, null=True, blank=True)
    approved_operation_codes = models.CharField(max_length=9, null=True, blank=True)
    aircraft_type = models.IntegerField(choices=AIRCRAFT_TYPE, null=True, blank=True)
    engine_type = models.IntegerField(choices=ENGINE_TYPE, null=True, blank=True)
    status_code = models.CharField(max_length=2, null=True, blank=True, choices=AIRCRAFT_STATUS_OPTIONS)
    mode_s_code = models.CharField(max_length=8, null=True, blank=True)
    fractional_ownership = models.CharField(max_length=1, null=True, blank=True)
    airworthiness_date = models.DateField(null=True, blank=True)
    other_name_1 = models.CharField(max_length=50, null=True, blank=True)
    other_name_2 = models.CharField(max_length=50, null=True, blank=True)
    other_name_3 = models.CharField(max_length=50, null=True, blank=True)
    other_name_4 = models.CharField(max_length=50, null=True, blank=True)
    other_name_5 = models.CharField(max_length=50, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    point = models.PointField(null=True, blank=True, srid=4326)

    objects = models.GeoManager()

    def manufacturer_model(self):
        try:
            return AircraftManufacturerCode.objects.get(code=self.aircraft_mfr_model_code)
        except AircraftManufacturerCode.DoesNotExist:
            return None

    def ownership(self):
        value = "%s: %s" % (self.get_type_registrant_display(), self.registrant_name)
        if self.other_name_1:
            value = value + ", " + self.other_name_1
        if self.other_name_2:
            value = value + ", " + self.other_name_2
        if self.other_name_3:
            value = value + ", " + self.other_name_3
        if self.other_name_4:
            value = value + ", " + self.other_name_4
        if self.other_name_5:
            value = value + ", " + self.other_name_5
        return value

    def get_absolute_url(self):
        return reverse('aircraft_detail', args=[self.n_number])

    def __unicode__(self):
        return self.n_number

