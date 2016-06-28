from django import template
from app.models import Species

register = template.Library()

@register.filter(name='ch')
def ch(value):
    y = str(value[0])
    return y.encode('utf-8')  

@register.filter(name='collapse')
def collapse(value):
    return ''.join(value.split())

@register.filter
def addstr(arg1,arg2):
    return str(arg1)+str(arg2)

@register.filter
def empty(value):
    if value=="None":
        return ''
    else:
        return value
