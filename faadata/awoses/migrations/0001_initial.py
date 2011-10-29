# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ('airports', '0001_initial'),
    )

    def forwards(self, orm):
        
        # Adding model 'AWOS'
        db.create_table('awoses_awos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('sensor_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('commissioned', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('frequency', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True)),
            ('second_frequency', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=3, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('airport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['airports.Airport'], null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('effective_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('awoses', ['AWOS'])


    def backwards(self, orm):
        
        # Deleting model 'AWOS'
        db.delete_table('awoses_awos')


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
        'awoses.awos': {
            'Meta': {'object_name': 'AWOS'},
            'airport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['airports.Airport']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'commissioned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'effective_date': ('django.db.models.fields.DateField', [], {}),
            'frequency': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'second_frequency': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'sensor_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '14'})
        }
    }

    complete_apps = ['awoses']
