from django import template

register = template.Library()

@register.filter(name='sliceindice')
def sliceindice(value,till):
    if type(value)==int:
        value = str(value)
    return value[:till]
@register.filter(name='sliceindicelast')
def sliceindicelast(value,fromm):
    if type(value)==int:
        value = str(value)
    return value[fromm:]