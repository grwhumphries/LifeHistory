"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from datetime import datetime
from app.models import Species, Traits


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'month':datetime.now().month,
            'day':datetime.now().day,
        })
    )


def lifehistory(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/lifehistory.html',
        context_instance = RequestContext(request,
        {
            'title':'lifehistory',
            'message':'the lifehistory database',
            'year':datetime.now().year,
            'month':datetime.now().month,
            'day':datetime.now().day,
        })
    )

def dbsearch(request):
    SpeciesList = Species.objects.all().order_by('species_id')
    X = Species.objects.all().distinct('ord').order_by('ord').values_list('ord')
    Y = Species.objects.all().distinct('fam').order_by('fam').values_list('fam')

    context = RequestContext(request, {'species':SpeciesList,'orders':X,'families':Y})
    template = loader.get_template('app/dbsearch.html')        
    return HttpResponse(template.render(context))
        
    
def dbadd(request):
    return render_to_response('app/dbadd.html')


def species(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        List = Species.objects.filter(species_id = l)
        traits = Traits.objects.filter(species__species_id = l)    

    context = RequestContext(request, {'LIST':List,'TRAITS':traits })
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))


def order(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        List = Species.objects.filter(ord = l)
    
    context = RequestContext(request, {'LIST':List})
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))


def family(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        List = Species.objects.filter(fam = l)
    
    context = RequestContext(request, {'LIST':List})
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))

def commonname(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        List = Species.objects.filter(common_name_1 = l)
    
    context = RequestContext(request, {'LIST':List})
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))
 