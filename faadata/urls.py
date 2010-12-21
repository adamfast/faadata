from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
)

if 'faadata.aircraft' in settings.INSTALLED_APPS:
    urlpatterns = urlpatterns + patterns('',
        (r'^aircraft/', include('faadata.aircraft.urls')),
    )

if 'faadata.airports' in settings.INSTALLED_APPS:
    urlpatterns = urlpatterns + patterns('',
        (r'^airports/', include('faadata.airports.urls')),
    )

if 'faadata.fixes' in settings.INSTALLED_APPS:
    urlpatterns = urlpatterns + patterns('',
        (r'^fixes/', include('faadata.fixes.urls')),
    )
