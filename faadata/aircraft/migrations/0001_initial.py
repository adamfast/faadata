# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftManufacturerCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=8, db_index=True)),
                ('manufacturer', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=20)),
                ('aircraft_type', models.CharField(max_length=1, choices=[(1, b'Glider'), (2, b'Balloon'), (3, b'Blimp/Dirigible'), (4, b'Fixed wing single engine'), (5, b'Fixed wing multi engine'), (6, b'Rotorcraft'), (7, b'Weight-shift-control'), (8, b'Powered Parachute'), (9, b'Gyroplane')])),
                ('engine_type', models.CharField(max_length=1, choices=[(0, b'None'), (1, b'Reciprocating'), (2, b'Turbo-prop'), (3, b'Turbo-shaft'), (4, b'Turbo-jet'), (5, b'Turbo-fan'), (6, b'Ramjet'), (7, b'2 Cycle'), (8, b'4 Cycle'), (9, b'Unknown')])),
                ('category', models.CharField(max_length=1, choices=[(1, b'Land'), (2, b'Sea'), (3, b'Amphibian')])),
                ('builder_certification_code', models.CharField(max_length=1, choices=[(0, b'Type Certificated'), (1, b'Not Type Certificated'), (2, b'Light Sport')])),
                ('number_of_engines', models.CharField(max_length=2)),
                ('number_of_seats', models.CharField(max_length=3)),
                ('aircraft_weight', models.CharField(max_length=7)),
                ('cruising_speed', models.CharField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AircraftRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n_number', models.CharField(max_length=5, db_index=True)),
                ('serial_number', models.CharField(max_length=30, null=True, blank=True)),
                ('aircraft_mfr_model_code', models.CharField(max_length=7, null=True, blank=True)),
                ('engine_mfr_model_code', models.CharField(max_length=5, null=True, blank=True)),
                ('year_mfg', models.CharField(max_length=4, null=True, blank=True)),
                ('type_registrant', models.IntegerField(blank=True, null=True, choices=[(1, b'Individual'), (2, b'Partnership'), (3, b'Corporation'), (4, b'Co-Owned'), (5, b'Government'), (8, b'Non-Citizen Corporation'), (9, b'Non-Citizen Co-Owned')])),
                ('registrant_name', models.CharField(max_length=50, null=True, blank=True)),
                ('street1', models.CharField(max_length=33, null=True, blank=True)),
                ('street2', models.CharField(max_length=33, null=True, blank=True)),
                ('city', models.CharField(max_length=18, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=10, null=True, blank=True)),
                ('region', models.CharField(blank=True, max_length=1, null=True, choices=[(1, b'Eastern'), (2, b'Southwestern'), (3, b'Central'), (4, b'Western-Pacific'), (5, b'Alaskan'), (7, b'Southern'), (8, b'European'), (b'C', b'Great Lakes'), (b'E', b'New England'), (b'S', b'Northwest Mountain')])),
                ('county', models.CharField(max_length=3, null=True, blank=True)),
                ('country', models.CharField(max_length=2, null=True, blank=True)),
                ('last_activity_date', models.DateField(null=True, blank=True)),
                ('certificate_issue_date', models.DateField(null=True, blank=True)),
                ('airworthiness_classification_code', models.CharField(blank=True, max_length=1, null=True, choices=[(1, b'Standard'), (2, b'Limited'), (3, b'Restricted'), (4, b'Experimental'), (5, b'Provisional'), (6, b'Multiple'), (7, b'Primary'), (8, b'Special Flight Permit'), (9, b'Light Sport')])),
                ('approved_operation_codes', models.CharField(max_length=9, null=True, blank=True)),
                ('aircraft_type', models.IntegerField(blank=True, null=True, choices=[(1, b'Glider'), (2, b'Balloon'), (3, b'Blimp/Dirigible'), (4, b'Fixed wing single engine'), (5, b'Fixed wing multi engine'), (6, b'Rotorcraft'), (7, b'Weight-shift-control'), (8, b'Powered Parachute'), (9, b'Gyroplane')])),
                ('engine_type', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Reciprocating'), (2, b'Turbo-prop'), (3, b'Turbo-shaft'), (4, b'Turbo-jet'), (5, b'Turbo-fan'), (6, b'Ramjet'), (7, b'2 Cycle'), (8, b'4 Cycle'), (9, b'Unknown')])),
                ('status_code', models.CharField(blank=True, max_length=2, null=True, choices=[(b'A', b'The Triennial Aircraft Registration form was mailed and has not been returned by the Post Office'), (b'D', b'Expired Dealer'), (b'E', b'The Certificate of Aircraft Registration was revoked by enforcement action'), (b'M', b'Aircraft registered to the manufacturer under their Dealer Certificate'), (b'N', b'Non-citizen Corporations which have not returned their flight hour reports'), (b'R', b'Registration pending'), (b'S', b'Second Triennial Aircraft Registration Form has been mailed'), (b'T', b'Valid Registration from a Trainee'), (b'V', b'Valid Registration'), (b'X', b'Enforcement Letter'), (b'Z', b'Permanent Reserved'), (b'1', b'Triennial Aircraft Registration form was returned by the Post Office as undeliverable'), (b'2', b'N-Number Assigned - but has not yet been registered'), (b'3', b'N-Number assigned as a Non Type Certificated aircraft - but has not yet been registered'), (b'4', b'N-Number assigned as import - but has not yet been registered'), (b'5', b'Reserved N-Number'), (b'6', b'Administratively canceled'), (b'7', b'Sale reported'), (b'8', b'A second attempt has been made at mailing a Triennial Aircraft Registration form to the owner with no response'), (b'9', b'Certificate of Registration has been revoked'), (b'10', b'N-Number assigned, has not been registered and is pending cancellation'), (b'11', b'N-Number assigned as a Non Type Certificated (Amateur) but has not been registered that is pending cancellation'), (b'12', b'N-Number assigned as import but has not been registered that is pending cancellation'), (b'13', b'Registration Expired'), (b'14', b'First Notice for Re-Registration/Renewal'), (b'15', b'Second Notice for Re-Registration/Renewal'), (b'16', b'Registration Expired - Pending Cancellation'), (b'17', b'Sale Reported - Pending Cancellation'), (b'18', b'Sale Reported - Canceled'), (b'19', b'Registration Pending - Pending Cancellation'), (b'20', b'Registration Pending - Canceled'), (b'21', b'Revoked - Pending Cancellation'), (b'22', b'Revoked - Canceled'), (b'23', b'Expired Dealer (Pending Cancellation)'), (b'24', b'Third Notice for Re-Registration/Renewal')])),
                ('mode_s_code', models.CharField(max_length=8, null=True, blank=True)),
                ('fractional_ownership', models.CharField(max_length=1, null=True, blank=True)),
                ('airworthiness_date', models.DateField(null=True, blank=True)),
                ('other_name_1', models.CharField(max_length=50, null=True, blank=True)),
                ('other_name_2', models.CharField(max_length=50, null=True, blank=True)),
                ('other_name_3', models.CharField(max_length=50, null=True, blank=True)),
                ('other_name_4', models.CharField(max_length=50, null=True, blank=True)),
                ('other_name_5', models.CharField(max_length=50, null=True, blank=True)),
                ('expiration_date', models.DateField(null=True, blank=True)),
                ('unique_id', models.CharField(max_length=8, null=True, blank=True)),
                ('kit_manufacturer', models.CharField(max_length=30, null=True, blank=True)),
                ('kit_model', models.CharField(max_length=20, null=True, blank=True)),
                ('mode_s_code_hex', models.CharField(max_length=10, null=True, blank=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('geocode_type', models.CharField(blank=True, max_length=2, null=True, choices=[(b'zi', b'Zip Code')])),
                ('geocode_date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
