"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

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
    return render_to_response('app/dbsearch.html') 

def dbadd(request):
    return render_to_response('app/dbadd.html') 