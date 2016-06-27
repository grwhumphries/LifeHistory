from django import template
from app.models import Species

register = template.Library()

@register.filter(name='ch')
def ch(value):
    y = str(value[0])
    return y.encode('utf-8')  
