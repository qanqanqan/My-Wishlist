from django import template


register = template.Library()

@register.filter(name='empty')
def empty(value):
    if len(value) == 0:
        return ' - '
    return value
