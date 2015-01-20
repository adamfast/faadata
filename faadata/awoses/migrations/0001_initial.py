# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AWOS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=5)),
                ('sensor_type', models.CharField(max_length=10)),
                ('commissioned', models.BooleanField(default=False)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('frequency', models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True)),
                ('second_frequency', models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True)),
                ('telephone', models.CharField(max_length=14)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=2)),
                ('effective_date', models.DateField()),
                ('airport', models.ForeignKey(blank=True, to='airports.Airport', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
