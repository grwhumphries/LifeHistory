from django import template
from app.models import Species, IucnData

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
    x = str(arg1).replace(' ','')
    y = str(arg2).replace(' ','')
    return x+y

@register.filter
def addstrnospace(arg1,arg2):
    return arg1+arg2

@register.filter
def empty(value):
    if value=="None":
        return ''
    else:
        return value

@register.filter
def range(value):
    if value == None:
        return ""
    else:
        return str(value.lower) + "-" + str(value.upper)


@register.filter
def ICUNstat(species_id):
    return str(IucnData.objects.filter(species_id = species_id).values_list('iucn_status')[0][0])

@register.filter
def ICUNtrend(species_id):
    return str(IucnData.objects.filter(species_id = species_id).values_list('population_trend')[0][0])

@register.filter
def Breedingdist(species_id):
    Breed = BreedingDistributions.objects.filter(species_id = species_id).values_list('breeding_distribution')
    blist = list()
    for b in Breed:
        blist.append(str(b[0]))
    return ",".join(blist)



