"""
Fragment rendering template tags.
"""

from django import template
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist
from django.template import Template
from fraggle.models import Fragment

register = template.Library()

@register.inclusion_tag("_fraggle_fragment.html", takes_context = True)
def render_fragment(context, fragment_title):
    """
    Render an html fragment.

    Usage::
        {% load render_fragment %}
        {% render_fragment 'title' %}

    """
    try: 
        fragment = Fragment.objects.get(title=fragment_title)
        content = force_unicode(smart_str(fragment.html))
        if "</form" in content:                                                      
            content = content.replace("</form>", "{% csrf_token %}</form>")
        content = mark_safe(Template(content).render(context))

    except Fragment.DoesNotExist:
        content = ""
        fragment = ""

    return dict(content = content, fragment = fragment)
