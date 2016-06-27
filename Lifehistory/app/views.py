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
    SpeciesList = Species.objects.all()
    X = list(set(Species.objects.all().values_list('order')))
    Y = list(set(Species.objects.all().values_list('family')))

    context = RequestContext(request, {'species':SpeciesList,'orders':X,'families':Y})
    template = loader.get_template('app/dbsearch.html')        
    return HttpResponse(template.render(context))
        
    
def dbadd(request):
    return render_to_response('app/dbadd.html')


def searchresult(request):
    List = Species.objects.filter()




 