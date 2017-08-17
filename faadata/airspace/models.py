# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Airspace(models.Model):
    ident = models.CharField(max_length=16, blank=True)  # appears to be airport identifier where the airspace is located
    name = models.CharField(max_length=128, blank=False)
    upper_desc = models.CharField(max_length=16)
    upper_val = models.IntegerField()
    upper_uom = models.CharField(max_length=16, blank=True)
    upper_code = models.CharField(max_length=16, blank=True)
    lower_desc = models.CharField(max_length=16)
    lower_val = models.IntegerField()
    lower_uom = models.CharField(max_length=16, blank=True)
    lower_code = models.CharField(max_length=16, blank=True)
    type_code = models.CharField(max_length=16)
    local_type = models.CharField(max_length=16)
    airspace_class = models.CharField(max_length=16)
    mil_code = models.CharField(max_length=16)
    comm_name = models.CharField(max_length=128, blank=True)
    level = models.CharField(max_length=16)
    sector = models.CharField(max_length=64, blank=True)
    onshore = models.IntegerField()
    exclusion = models.IntegerField()
    wkhr_code = models.CharField(max_length=16)
    wkhr_remark = models.CharField(max_length=128, blank=True)
    mpoly = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.name
