from django import template
from django.forms import BoundField

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    if isinstance(value, BoundField):
        existing_attrs = value.field.widget.attrs
        existing_attrs['class'] = arg
        return value.as_widget(attrs=existing_attrs)
    return value