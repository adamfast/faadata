from django.conf import settings
from django.conf.urls.defaults import *

from faadata.aircraft.models import *

aircraft_list = AircraftRegistration.objects.all().order_by('n_number')

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-zA-Z0-9*.]+)/$', 'django.views.generic.list_detail.object_detail', {'queryset': aircraft_list, 'slug_field': 'n_number'}, name='aircraft_detail'),
    (r'^$', 'django.views.generic.list_detail.object_list', {'queryset': aircraft_list, 'paginate_by': getattr(settings, 'AIRCRAFT_PAGINATE_BY', 20)}),
)
