# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ('aircraft', '0001_initial'),
    )

    def forwards(self, orm):
        
        # Adding field 'AircraftRegistration.expiration_date'
        db.add_column('aircraft_aircraftregistration', 'expiration_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'AircraftRegistration.expiration_date'
        db.delete_column('aircraft_aircraftregistration', 'expiration_date')


    models = {
        'aircraft.aircraftmanufacturercode': {
            'Meta': {'object_name': 'AircraftManufacturerCode'},
            'aircraft_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'aircraft_weight': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'builder_certification_code': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cruising_speed': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'engine_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'number_of_engines': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'number_of_seats': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'aircraft.aircraftregistration': {
            'Meta': {'object_name': 'AircraftRegistration'},
            'aircraft_mfr_model_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'aircraft_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'airworthiness_classification_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'airworthiness_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'approved_operation_codes': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'certificate_issue_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'engine_mfr_model_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'engine_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fractional_ownership': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_activity_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'mode_s_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'n_number': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'other_name_1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'other_name_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'other_name_3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'other_name_4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'other_name_5': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'registrant_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '33', 'null': 'True', 'blank': 'True'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '33', 'null': 'True', 'blank': 'True'}),
            'type_registrant': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year_mfg': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['aircraft']
