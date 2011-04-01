#!/home/bin/python
# -*- coding: utf-8
from django.contrib.gis.geos import Point
from decimal import Decimal
from faadata.fixes.models import *
from faddsdata.natfix import parse_natfix_file

def natfix_import(importfile):
    fixes = parse_natfix_file(importfile)

    for fix in fixes:
        try:
            f = Fix.objects.get(id=fix['id'])
        except Fix.DoesNotExist:
            f = Fix(id=fix['id'])
        f.point = Point((fix['lon'], fix['lat']))
        f.artcc = fix['artcc_id']
        f.state_post_office_code = fix['state_code']
        f.fix_type = fix['fix_navaid_type']
        f.save()
