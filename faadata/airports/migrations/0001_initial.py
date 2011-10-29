# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Airport'
        db.create_table('airports_airport', (
            ('facility_site_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11, primary_key=True)),
            ('location_identifier', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('facility_name', self.gf('django.db.models.fields.CharField')(max_length=42)),
            ('ownership_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('use_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('owners_name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('facility_manager_name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('elevation_msl', self.gf('django.db.models.fields.IntegerField')()),
            ('traffic_pattern_agl', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('activation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('control_tower', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ctaf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True)),
            ('segmented_circle', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('beacon_color', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('landing_fees', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medical_use', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('singles_based', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('multis_based', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('jets_based', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('helicopters_based', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('gliders_based', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('military_based', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ultralights_based', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('icao_identifier', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal('airports', ['Airport'])

        # Adding model 'Remark'
        db.create_table('airports_remark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('airport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['airports.Airport'])),
            ('element_name', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('airports', ['Remark'])

        # Adding model 'Attendance'
        db.create_table('airports_attendance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('airport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['airports.Airport'])),
            ('sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('schedule', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('airports', ['Attendance'])

        # Adding model 'Runway'
        db.create_table('airports_runway', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('airport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['airports.Airport'])),
            ('runway_identification', self.gf('django.db.models.fields.CharField')(max_length='7')),
            ('runway_length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('runway_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('surface_type_condition', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('surface_treatment', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('pavement_classification_number', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('lights_edge_intensity', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('base_end_point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('base_end_elevation_physical_runway_end', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('base_end_displaced_threshold_point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('base_end_elevation_displaced_threshold', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('base_end_displaced_threshold_length_from_end', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('base_end_visual_glide_slope_indicators', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('base_end_runway_visual_range_equipment_locations', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('base_end_runway_visual_range_equipment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reciprocal_end_point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('reciprocal_end_elevation_physical_runway_end', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('reciprocal_end_displaced_threshold_point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('reciprocal_end_elevation_displaced_threshold', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('reciprocal_end_displaced_threshold_length_from_end', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('reciprocal_end_visual_glide_slope_indicators', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('reciprocal_end_runway_visual_range_equipment_locations', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('reciprocal_end_runway_visual_range_equipment', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('airports', ['Runway'])


    def backwards(self, orm):
        
        # Deleting model 'Airport'
        db.delete_table('airports_airport')

        # Deleting model 'Remark'
        db.delete_table('airports_remark')

        # Deleting model 'Attendance'
        db.delete_table('airports_attendance')

        # Deleting model 'Runway'
        db.delete_table('airports_runway')


    models = {
        'airports.airport': {
            'Meta': {'object_name': 'Airport'},
            'activation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'beacon_color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'control_tower': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ctaf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'elevation_msl': ('django.db.models.fields.IntegerField', [], {}),
            'facility_manager_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'facility_name': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'facility_site_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11', 'primary_key': 'True'}),
            'gliders_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'helicopters_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icao_identifier': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'jets_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'landing_fees': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_identifier': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'medical_use': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'military_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'multis_based': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
