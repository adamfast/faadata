from django import template
from django.conf import settings

register = template.Library()

@register.filter
def perday(value):
	return int(round(value / 365.24));

# source: http://djangosnippets.org/snippets/1391/
@register.filter
def pluspagecount(value, page):
    value, page = int(value), int(page)
    adjusted_value = value + ((page - 1) * getattr(settings, "AIRPORTS_PAGINATE_BY", 50))
    return adjusted_value