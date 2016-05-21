# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='associated_city',
            field=models.CharField(default=b'', max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='airport',
            name='associated_state_name',
            field=models.CharField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
