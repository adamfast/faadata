# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fix',
            fields=[
                ('id', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('artcc', models.CharField(max_length=4, db_index=True)),
                ('state_post_office_code', models.CharField(max_length=2)),
                ('fix_type', models.CharField(max_length=8, db_index=True)),
            ],
            options={
                'verbose_name_plural': 'Fixes',
            },
            bases=(models.Model,),
        ),
    ]
