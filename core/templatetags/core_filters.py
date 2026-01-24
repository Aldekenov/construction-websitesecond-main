from django import template

register = template.Library()

@register.filter
def split(value, delimiter="\n"):
    return value.split(delimiter)