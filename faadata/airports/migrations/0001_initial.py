# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('facility_site_number', models.CharField(max_length=11, unique=True, serialize=False, primary_key=True)),
                ('location_identifier', models.CharField(unique=True, max_length=7)),
                ('facility_name', models.CharField(max_length=50)),
                ('facility_type', models.CharField(max_length=16)),
                ('associated_state_post_office_code', models.CharField(max_length=2)),
                ('ownership_type', models.CharField(max_length=2, choices=[(b'PU', b'PUBLICLY OWNED'), (b'PR', b'PRIVATELY OWNED'), (b'MA', b'AIR FORCE OWNED'), (b'MN', b'NAVY OWNED'), (b'MR', b'ARMY OWNED')])),
                ('use_type', models.CharField(max_length=2, choices=[(b'PU', b'OPEN TO THE PUBLIC'), (b'PR', b'PRIVATE')])),
                ('owners_name', models.CharField(max_length=35)),
                ('facility_manager_name', models.CharField(max_length=35)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('elevation_msl', models.DecimalField(max_digits=7, decimal_places=1)),
                ('traffic_pattern_agl', models.IntegerField(null=True, blank=True)),
                ('activation_date', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=2, choices=[(b'CI', b'CLOSED INDEFINITELY'), (b'CP', b'CLOSED PERMANENTLY'), (b'O', b'OPERATIONAL')])),
                ('control_tower', models.BooleanField(default=False)),
                ('ctaf', models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True)),
                ('segmented_circle', models.BooleanField(default=False)),
                ('beacon_color', models.CharField(max_length=3)),
                ('landing_fees', models.BooleanField(default=False)),
                ('medical_use', models.BooleanField(default=False)),
                ('singles_based', models.IntegerField(default=0)),
                ('multis_based', models.IntegerField(default=0)),
                ('jets_based', models.IntegerField(default=0)),
                ('helicopters_based', models.IntegerField(default=0)),
                ('gliders_based', models.IntegerField(default=0)),
                ('military_based', models.IntegerField(default=0)),
                ('ultralights_based', models.IntegerField(default=0)),
                ('icao_identifier', models.CharField(max_length=7)),
                ('commercial_services_operations', models.IntegerField(default=0)),
                ('commuter_services_operations', models.IntegerField(default=0)),
                ('air_taxi_operations', models.IntegerField(default=0)),
                ('ga_local_operations', models.IntegerField(default=0)),
                ('ga_itinerant_operations', models.IntegerField(default=0)),
                ('military_operations', models.IntegerField(default=0)),
                ('operations_ending_date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.IntegerField()),
                ('schedule', models.TextField()),
                ('airport', models.ForeignKey(to='airports.Airport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element_name', models.CharField(max_length=13)),
                ('body', models.TextField()),
                ('airport', models.ForeignKey(to='airports.Airport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Runway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runway_identification', models.CharField(max_length=b'7')),
                ('runway_length', models.IntegerField(null=True, blank=True)),
                ('runway_width', models.IntegerField(null=True, blank=True)),
                ('surface_type_condition', models.CharField(max_length=14, null=True, blank=True)),
                ('surface_treatment', models.CharField(max_length=8, null=True, blank=True)),
                ('pavement_classification_number', models.CharField(max_length=14, null=True, blank=True)),
                ('lights_edge_intensity', models.CharField(max_length=8, null=True, blank=True)),
                ('base_end_point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('base_end_elevation_physical_runway_end', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('base_end_displaced_threshold_point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('base_end_elevation_displaced_threshold', models.IntegerField(null=True, blank=True)),
                ('base_end_displaced_threshold_length_from_end', models.IntegerField(null=True, blank=True)),
                ('base_end_visual_glide_slope_indicators', models.CharField(max_length=8, null=True, blank=True)),
                ('base_end_runway_visual_range_equipment_locations', models.CharField(max_length=8, null=True, blank=True)),
                ('base_end_runway_visual_range_equipment', models.BooleanField(default=False)),
                ('reciprocal_end_point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('reciprocal_end_elevation_physical_runway_end', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('reciprocal_end_displaced_threshold_point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('reciprocal_end_elevation_displaced_threshold', models.IntegerField(null=True, blank=True)),
                ('reciprocal_end_displaced_threshold_length_from_end', models.IntegerField(null=True, blank=True)),
                ('reciprocal_end_visual_glide_slope_indicators', models.CharField(max_length=8, null=True, blank=True)),
                ('reciprocal_end_runway_visual_range_equipment_locations', models.CharField(max_length=8, null=True, blank=True)),
                ('reciprocal_end_runway_visual_range_equipment', models.BooleanField(default=False)),
                ('airport', models.ForeignKey(to='airports.Airport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
