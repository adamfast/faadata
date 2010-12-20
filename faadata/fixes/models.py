from django.contrib.gis.db import models

class Fix(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    point = models.PointField(srid=4326)
    artcc = models.CharField(max_length=4, db_index=True)
    state_post_office_code = models.CharField(max_length=2)
    fix_type = models.CharField(max_length=8, db_index=True)

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Fixes'
