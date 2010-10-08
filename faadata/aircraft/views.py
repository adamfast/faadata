from django import forms
from django.contrib.localflavor.us.forms import USStateField
from django.core.cache import cache
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from faadata.aircraft.models import *

class search_form(forms.Form):
    model = forms.CharField(label='Aircraft Model')
    state = USStateField(required=False)

def find_aircraft(request):
    if request.GET.get('model', None):
        form = search_form(request.GET)
        if form.is_valid():
            model_code_cache_key = 'aircraftmodelcode|%s' % form.cleaned_data['model']
            model_codes = cache.get(model_code_cache_key)
            if not model_codes:
                models = AircraftManufacturerCode.objects.filter(model__icontains=form.cleaned_data['model']).order_by('code')
                model_codes = [obj.code for obj in models]
                cache.set(model_code_cache_key, model_codes, 12 * 60 * 60) # cache 12 hours

            airplanes_cache_key = 'airplanes|%s|%s' % (form.cleaned_data['model'], form.cleaned_data['state'])
            airplanes = cache.get(airplanes_cache_key)
            if not airplanes:
                airplanes = AircraftRegistration.objects.filter(aircraft_mfr_model_code__in=model_codes).order_by('n_number')
                if form.cleaned_data['state']:
                    airplanes = airplanes.filter(state=form.cleaned_data['state'])
                cache.set(airplanes_cache_key, airplanes, 12 * 60 * 60) # cache 12 hours

            return object_list(request, queryset=airplanes, template_name='aircraft/find_model.html', paginate_by=50, extra_context={'form': form, 'model': form.cleaned_data['model'], 'state': form.cleaned_data['state']})
    else:
        form = search_form()

    return render_to_response('aircraft/find_model.html', {'form': form})
