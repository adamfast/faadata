# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Airport.commercial_services_operations'
        db.add_column('airports_airport', 'commercial_services_operations', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Airport.commuter_services_operations'
        db.add_column('airports_airport', 'commuter_services_operations', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Airport.air_taxi_operations'
        db.add_column('airports_airport', 'air_taxi_operations', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Airport.ga_local_operations'
        db.add_column('airports_airport', 'ga_local_operations', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Airport.ga_itinerant_operations'
        db.add_column('airports_airport', 'ga_itinerant_operations', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Airport.military_operations'
        db.add_column('airports_airport', 'military_operations', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Airport.operations_ending_date'
        db.add_column('airports_airport', 'operations_ending_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Airport.commercial_services_operations'
        db.delete_column('airports_airport', 'commercial_services_operations')

        # Deleting field 'Airport.commuter_services_operations'
        db.delete_column('airports_airport', 'commuter_services_operations')

        # Deleting field 'Airport.air_taxi_operations'
        db.delete_column('airports_airport', 'air_taxi_operations')

        # Deleting field 'Airport.ga_local_operations'
        db.delete_column('airports_airport', 'ga_local_operations')

        # Deleting field 'Airport.ga_itinerant_operations'
        db.delete_column('airports_airport', 'ga_itinerant_operations')

        # Deleting field 'Airport.military_operations'
        db.delete_column('airports_airport', 'military_operations')

        # Deleting field 'Airport.operations_ending_date'
        db.delete_column('airports_airport', 'operations_ending_date')


    models = {
        'airports.airport': {
            'Meta': {'object_name': 'Airport'},
            'activation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'air_taxi_operations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'beacon_color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'commercial_services_operations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'commuter_services_operations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'control_tower': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ctaf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'elevation_msl': ('django.db.models.fields.IntegerField', [], {}),
            'facility_manager_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'facility_name': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'facility_site_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11', 'primary_key': 'True'}),
            'ga_itinerant_operations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ga_local_operations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gliders_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'helicopters_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icao_identifier': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'jets_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'landing_fees': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_identifier': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'medical_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'military_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'military_operations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'multis_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'operations_ending_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'owners_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'ownership_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'segmented_circle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'singles_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'traffic_pattern_agl': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ultralights_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'use_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'airports.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'airport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['airports.Airport']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schedule': ('django.db.models.fields.TextField', [], {}),
            'sequence': ('django.db.models.fields.IntegerField', [], {})
        },
        'airports.remark': {
            'Meta': {'object_name': 'Remark'},
            'airport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['airports.Airport']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'element_name': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'airports.runway': {
            'Meta': {'object_name': 'Runway'},
            'airport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['airports.Airport']"}),
            'base_end_displaced_threshold_length_from_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'base_end_displaced_threshold_point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'base_end_elevation_displaced_threshold': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'base_end_elevation_physical_runway_end': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'base_end_point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'base_end_runway_visual_range_equipment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'base_end_runway_visual_range_equipment_locations': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'base_end_visual_glide_slope_indicators': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lights_edge_intensity': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'pavement_classification_number': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'reciprocal_end_displaced_threshold_length_from_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reciprocal_end_displaced_threshold_point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'reciprocal_end_elevation_displaced_threshold': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reciprocal_end_elevation_physical_runway_end': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'reciprocal_end_point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'reciprocal_end_runway_visual_range_equipment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reciprocal_end_runway_visual_range_equipment_locations': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'reciprocal_end_visual_glide_slope_indicators': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'runway_identification': ('django.db.models.fields.CharField', [], {'max_length': "'7'"}),
            'runway_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'runway_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'surface_treatment': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'surface_type_condition': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['airports']
