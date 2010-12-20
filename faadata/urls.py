from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'airports/', include('faadata.airports.urls')),
)
