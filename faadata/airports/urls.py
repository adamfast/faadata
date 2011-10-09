from django.conf import settings
from django.conf.urls.defaults import *

from faadata.airports.models import *

airport_list = Airport.objects.all().order_by('location_identifier')

_ops_per_day = r'''commercial_services_operations + commuter_services_operations +
                   air_taxi_operations + ga_local_operations +
                   ga_itinerant_operations + military_operations'''
_ga_ops_per_day = r'''ga_local_operations + ga_itinerant_operations'''
airport_ops_list = Airport.objects.extra(select={"total_ops": _ops_per_day,
                                                 "ga_ops": _ga_ops_per_day},
										 order_by = ['-ga_ops'])

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-zA-Z0-9*.]+)/$', 'django.views.generic.list_detail.object_detail', {'queryset': airport_list, 'slug_field': 'location_identifier'}, name='airport_detail'),
    (r'^$', 'django.views.generic.list_detail.object_list', {'queryset': airport_list, 'paginate_by': getattr(settings, 'AIRPORTS_PAGINATE_BY', 20)}),

    (r'^ops$', 
        'django.views.generic.list_detail.object_list',
        { 'queryset': airport_ops_list,
          'paginate_by': getattr(settings, 'AIRPORTS_PAGINATE_BY', 50),
          'template_name': 'airports/airport_ops_list.html' }),
)
