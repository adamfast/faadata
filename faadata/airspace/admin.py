# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from faadata.airspace.models import *


class AirspaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'ident', 'airspace_class', 'level', 'sector', 'upper_desc', 'upper_val', 'upper_uom', 'upper_code', 'lower_desc', 'lower_val', 'lower_uom', 'lower_code')

admin.site.register(Airspace, AirspaceAdmin)
