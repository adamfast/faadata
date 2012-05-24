from django.conf import settings
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

class Fix(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    point = models.PointField(srid=4326)
    artcc = models.CharField(max_length=4, db_index=True)
    state_post_office_code = models.CharField(max_length=2)
    fix_type = models.CharField(max_length=8, db_index=True)

    objects = models.GeoManager()

    def get_absolute_url(self):
        return reverse('fix_detail', args=[self.id])

    def locator_point(self):
        return self.point

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Fixes'

# integrate with the django-locator app for easy geo lookups if it's installed
if 'locator.objects' in settings.INSTALLED_APPS:
    from locator.objects.models import create_locator_object
    models.signals.post_save.connect(create_locator_object, sender=Fix)
