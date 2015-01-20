# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Fix'
        db.create_table('fixes_fix', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=8, primary_key=True)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('artcc', self.gf('django.db.models.fields.CharField')(max_length=4, db_index=True)),
            ('state_post_office_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fix_type', self.gf('django.db.models.fields.CharField')(max_length=8, db_index=True)),
        ))
        db.send_create_signal('fixes', ['Fix'])


    def backwards(self, orm):
        
        # Deleting model 'Fix'
        db.delete_table('fixes_fix')


    models = {
        'fixes.fix': {
            'Meta': {'object_name': 'Fix'},
            'artcc': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_index': 'True'}),
            'fix_type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_index': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'state_post_office_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['fixes']
