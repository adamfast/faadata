from django.conf import settings
from django.conf.urls.defaults import *

from faadata.fixes.models import *

fix_list = Fix.objects.all().order_by('id')

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-zA-Z0-9*.]+)/$', 'django.views.generic.list_detail.object_detail', {'queryset': fix_list, 'slug_field': 'id'}, name='fix_detail'),
    (r'^$', 'django.views.generic.list_detail.object_list', {'queryset': fix_list, 'paginate_by': getattr(settings, 'FIXES_PAGINATE_BY', 20)}),
)
