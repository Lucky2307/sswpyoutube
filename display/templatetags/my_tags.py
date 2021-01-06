from django import template
from django.template.defaultfilters import stringfilter
from urllib.parse import urlencode

register = template.Library()

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    if query.get('page'):
        query.pop('page')
    query.update(kwargs)
    return query.urlencode()