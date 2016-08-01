"""
Definition of views.
"""
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from datetime import datetime
from app.models import *
from app.forms import PostForm, PostFormOther
from djqscsv import render_to_csv_response
import csv


def entrykey(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/EntryKey.html',
        context_instance = RequestContext(request,
        {
            'title':'Database Key legend',
            'year':datetime.now().year,
            'month':datetime.now().month,
            'day':datetime.now().day,
        })
    )

def dbaddother(request):
    modelform = PostFormOther()
    SpeciesList = Species.objects.all().order_by('species_id')
    traitslist = OtherTraits.objects.all().distinct('variable')
    citations = Citation.objects.all()
    X = Traitnames.objects.filter(variable = "coloniality")
    

    context = RequestContext(request, {'species':SpeciesList,
                                       'citations':citations,
                                       'traits':traitslist,
                                       'traitopts':X,
                                       'modelform':modelform,                                       
                                       'year':datetime.now().year,
                                       'month':datetime.now().month,
                                       'day':datetime.now().day, })
    template = loader.get_template('app/dbaddother.html')        
    return HttpResponse(template.render(context))



def chartraits(request):
    if request.method == 'GET':
        chartrait = request.GET.get('ct','')
        X = Traitnames.objects.filter(variable = chartrait)
    else:
        X = []
    context = RequestContext(request, {'traitopts':X})
    template = loader.get_template('app/chartraits.html')        
    return HttpResponse(template.render(context))





def dbadd(request):
    modelform = PostForm()
    SpeciesList = Species.objects.all().order_by('species_id')
    traitslist = NumericTraits.objects.all().distinct('traits')
    unitslist = NumericTraits.objects.all().distinct('units')
    citations = Citation.objects.all()

    context = RequestContext(request, {'species':SpeciesList,
                                       'citations':citations,
                                       'numtraits':traitslist,
                                       'units':unitslist,
                                       'modelform':modelform,
                                       'year':datetime.now().year,
                                       'month':datetime.now().month,
                                       'day':datetime.now().day, })
    template = loader.get_template('app/dbadd.html')        
    return HttpResponse(template.render(context))



@csrf_exempt  ## NOTE - this is required to get past the 403 forbidden error when using an Ajax call for saving
def dbPost(request):
    args = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save( commit = False)
            post.feature_id = request.POST.get("feature_id", "")
            specId = request.POST.get("species", "")            
            citeId = request.POST.get("citation", "")            
            post.username = request.POST.get("username", "")
            post.dt = request.POST.get("dt", "")            
            post.species_id = Species.objects.get(species_id_html = specId)
            post.traits = request.POST.get("traits", "")            
            if request.POST.get("mean","") == "":
                post.mean = None
            else:
                post.mean = int(request.POST.get("mean",""))
            
            if request.POST.get("range0","") == "":
                r1 = None
            else: 
                r1 = int(request.POST.get("range0",""))
            if request.POST.get("range1","") == "":
                r2 = None
            else:
                r2 = int(request.POST.get("range1",""))
                                            
            post.range = [r1,r2]
            
            
            post.uncertainty = request.POST.get("uncertainty","")
            post.units = request.POST.get("units","")
            post.cite = Citation.objects.get(citation_name = citeId)
            
            post.save()

            cnt = CitationNumerictraitSpecies()
            cnt.relation_id = CitationNumerictraitSpecies.objects.all().order_by('-relation_id').values_list()[0][0] + 1
            cnt.feature = NumericTraits.objects.get(feature_id = request.POST.get("feature_id", ""))
            cnt.cite = Citation.objects.get(citation_name = citeId)
            cnt.species = Species.objects.get(species_id_html = specId)
            cnt.save()
        
            return HttpResponse('')        
        else:
            print form.errors                       
           
    else:
        form = PostFormOther()
    
        args['form'] = form
        return render(request, 'app/lifehistory.html', args)



@csrf_exempt
def dbPostother(request):
    
    args = {}
    if request.method == 'POST':
    #if request.is_ajax():
        form = PostFormOther(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.trt_id = request.POST.get("trtid", "")
            specId = request.POST.get("species", "")
            post.username = request.POST.get("username", "")
            post.dt = request.POST.get("dt", "")            
            post.species_id = Species.objects.get(species_id_html = specId)
            post.value = request.POST.get("traitopt","")
            citeId = request.POST.get("citation", "")
            post.cite = Citation.objects.get(citation_name = citeId)
            post.variable = request.POST.get("traits","")
            post.study_year = request.POST.get("study_year","")            
            post.study_location = request.POST.get("study_location","")
            comments = request.POST.get("comments","")
            print comments
                                      
            post.save()

            cots = CitationOthertraitSpecies()
            cots.relation_id = CitationOthertraitSpecies.objects.all().order_by('-relation_id').values_list()[0][0] + 1
            cots.trt = OtherTraits.objects.get(trt_id = request.POST.get("trtid", ""))
            cots.cite = Citation.objects.get(citation_name = citeId)
            cots.species = Species.objects.get(species_id_html = specId)
            cots.save()
            
            
            return HttpResponse('')        
        else:
            print form.errors                       
           
    else:
        form = PostFormOther()
    
        args['form'] = form
        return render(request, 'app/lifehistory.html', args)
        



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
       
    all = NumericTraits.objects.all().select_related()
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
            'alldat':all
        })
    )



#def downloadall(request):
    #all = NumericTraits.objects.all().values('species__ord', 'species__fam', 'species__genus', 'species__species','species__subspecies','traits','mean','range','uncertainty','units','cite__citation_name')    
    #return render_to_csv_response(all)

    
def downloadCommon(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        dl = request.GET.get('DL','')
        if dl == "dlNum":        
            all = NumericTraits.objects.filter(species_id = l).values('species__ord', 'species__fam', 'species_id','traits','mean','range','uncertainty','units','cite__citation_name')    
        elif dl == "dlChar":
            all = OtherTraits.objects.filter(species_id = l).values('species__ord', 'species__fam', 'species_id','variable','value','cite__citation_name')    
        elif dl == "dlCite":
            X = [x.cite.citation_name for x in CitationNumerictraitSpecies.objects.filter(species_id = l).distinct('cite__citation_name')]
            Y = [y.cite.citation_name for y in CitationOthertraitSpecies.objects.filter(species_id = l).distinct('cite__citation_name')]
            Z = X + Y
            alist = list(set(Z))
            all = Citation.objects.filter(citation_name__in = alist).values('citation_name','citation')

    return render_to_csv_response(all)

def downloadSpecies(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        dl = request.GET.get('DL','')
        if dl == "dlNum":        
            all = NumericTraits.objects.filter(species_id = l).values('species__ord', 'species__fam', 'species_id','traits','mean','range','uncertainty','units','cite__citation_name')    
        elif dl == "dlChar":
            all = OtherTraits.objects.filter(species_id = l).values('species__ord', 'species__fam', 'species_id','variable','value','cite__citation_name')    
        elif dl == "dlCite":
            X = [x.cite.citation_name for x in CitationNumerictraitSpecies.objects.filter(species_id = l).distinct('cite__citation_name')]
            Y = [y.cite.citation_name for y in CitationOthertraitSpecies.objects.filter(species_id = l).distinct('cite__citation_name')]
            Z = X + Y
            alist = list(set(Z))
            all = Citation.objects.filter(citation_name__in = alist).values('citation_name','citation')
                      
    return render_to_csv_response(all)

def downloadOrder(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        dl = request.GET.get('DL','')
        if dl == "dlNum":        
            all = NumericTraits.objects.filter(species__ord = l).values('species__ord', 'species__fam', 'species_id','traits','mean','range','uncertainty','units','cite__citation_name')    
        elif dl == "dlChar":
            all = OtherTraits.objects.filter(species__ord = l).values('species__ord', 'species__fam', 'species_id','variable','value','cite__citation_name')    
        elif dl == "dlCite":
            X = [x.cite.citation_name for x in CitationNumerictraitSpecies.objects.filter(species__ord = l).distinct('cite__citation_name')]
            Y = [y.cite.citation_name for y in CitationOthertraitSpecies.objects.filter(species__ord = l).distinct('cite__citation_name')]
            Z = X + Y
            alist = list(set(Z))
            all = Citation.objects.filter(citation_name__in = alist).values('citation_name','citation')

        all = NumericTraits.objects.filter(species__ord = l).values('species__ord', 'species__fam', 'species__genus', 'species__species','species__subspecies','traits','mean','range','uncertainty','units','cite__citation_name')    
    return render_to_csv_response(all)


def downloadFamily(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        dl = request.GET.get('DL','')
        if dl == "dlNum":        
            all = NumericTraits.objects.filter(species__fam = l).values('species__ord', 'species__fam', 'species_id','traits','mean','range','uncertainty','units','cite__citation_name')    
        elif dl == "dlChar":
            all = OtherTraits.objects.filter(species__fam = l).values('species__ord', 'species__fam', 'species_id','variable','value','cite__citation_name')    
        elif dl == "dlCite":
            X = [x.cite.citation_name for x in CitationNumerictraitSpecies.objects.filter(species__fam = l).distinct('cite__citation_name')]
            Y = [y.cite.citation_name for y in CitationOthertraitSpecies.objects.filter(species__fam = l).distinct('cite__citation_name')]
            Z = X + Y
            alist = list(set(Z))
            all = Citation.objects.filter(citation_name__in = alist).values('citation_name','citation')

    return render_to_csv_response(all)








def dbsearch(request):
    SpeciesList = Species.objects.all().order_by('species_id')
    CnameList = CommonNames.objects.all().order_by('common_name')
    X = Species.objects.all().distinct('ord').order_by('ord').values_list('ord')
    Y = Species.objects.all().distinct('fam').order_by('fam').values_list('fam')

    context = RequestContext(request, {'commonnames':CnameList,'species':SpeciesList,'orders':X,'families':Y})
    template = loader.get_template('app/dbsearch.html')        
    return HttpResponse(template.render(context))
        
   


def species(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        CommName = CommonNames.objects.filter(species_id = l).filter(common_name_id = 1).select_related()
            
    context = RequestContext(request, {'CommName':CommName})
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))


def order(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        CommName = CommonNames.objects.filter(species__ord = l).filter(common_name_id = 1).select_related()
    
    context = RequestContext(request, {'CommName':CommName})
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))


def family(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        CommName = CommonNames.objects.filter(species__fam = l).filter(common_name_id = 1).select_related()
                                
    context = RequestContext(request, {'CommName':CommName})
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))




def commonname(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        CommName = CommonNames.objects.filter(species_id = l).filter(common_name_id = 1).select_related()
        
    context = RequestContext(request, {'CommName':CommName})
    template = loader.get_template('app/searchresult.html')        
    return HttpResponse(template.render(context))



def numerictraits(request):
    if request.method == 'GET':
        l = request.GET.get('l','')
        Numtraits = NumericTraits.objects.filter(species_id = l).order_by('traits','-feature_id').select_related('cite') 

    context = RequestContext(request, {'LIST':Numtraits})
    template = loader.get_template('app/numerictraits.html')        
    return HttpResponse(template.render(context))


def charactertraits(request):
    if request.method == 'GET':
        l = request.GET.get('l','')
                
        Chtraits = OtherTraits.objects.filter(species_id = l).order_by('variable','-trt_id').select_related('cite')        
        Breed = BreedingDistributions.objects.filter(species_id = l).select_related('cite')
        Nests = NestLocations.objects.filter(species_id = l).select_related('cite')

    context = RequestContext(request, {'chLIST':Chtraits,'Breed':Breed,'Nests':Nests})
    template = loader.get_template('app/charactertraits.html')        
    return HttpResponse(template.render(context))




############################################################################################

