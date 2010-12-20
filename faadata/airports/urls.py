from django.conf import settings
from django.conf.urls.defaults import *

from faadata.airports.models import *

airport_list = Airport.objects.all().order_by('location_identifier')

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', {'queryset': airport_list, 'paginate_by': getattr(settings, 'AIRPORTS_PAGINATE_BY', 20)}),
)
