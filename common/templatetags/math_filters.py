from django import template


register = template.Library()


@register.filter
def intdiv(value, arg):
    """Integer division filter"""
    return int(value) // int(arg)
