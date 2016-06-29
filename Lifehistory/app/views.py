"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from datetime import datetime
from app.models import Species, Traits
from djqscsv import render_to_csv_response
import csv

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
          
    all = Traits.objects.all().select_related()
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

def downloadall(request):    
    all = Traits.objects.all().values('species__fid', 'species__ord', 'species__fam', 'species__genus', 'species__species', 'species__species_id', 'species__synonyms', 'species__common_name_1', 'species__common_name_2', 'species__common_name_3', 'species__common_name_4', 'species__common_name_5', 'species__common_name_6', 'species__iucn_status', 'species__red_list_criteria', 'species__year_assessed', 'species__population_trend', 'species__coloniality', 'species__breeding_dist', 'species__nest_locations', 'species__hatchling_type', 'female_mass_mean', 'female_mass_upper', 'female_mass_lower', 'female_mass_uncertainty', 'male_mass_mean', 'male_mass_lower', 'male_mass_upper', 'male_mass_uncertainty', 'clutch_size_mean', 'clutch_size_lower', 'cluth_size_upper', 'clutch_size_uncertainty', 'clutch_interval', 'incubation_mean', 'incubation_period_lower', 'incubtaion_period_upper', 'incubation_period_uncertainty', 'fledging_period_mean', 'fledging_period_lower', 'fledging_period_upper', 'fledging_period_uncertainty', 'max_growth_mean', 'max_growth_lower', 'max_growth_upper', 'max_growth_uncertainty', 'post_fledge_care_mean', 'post_fledge_care_lower', 'post_fledge_care_upper', 'post_fledge_care_uncertainty', 'age_first_breed_mean', 'age_first_breed_lower', 'age_first_breed_upper', 'age_first_breed_uncertainty', 'foraging_distance', 'wingspan_mean', 'wingspan_lower', 'wingspan_upper', 'wingspan_uncertainty', 'max_age_mean', 'max_age_lower', 'max_age_upper', 'max_age_uncertainty', 'annual_survival_mean', 'annual_survival_lower', 'annual_survival_upper', 'annual_survival_uncertainty', 'citation', 'username', 'dt')
    return render_to_csv_response(all)
    
def downloadCommon(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        all = Traits.objects.filter(species__common_name_1 = l).values('species__fid', 'species__ord', 'species__fam', 'species__genus', 'species__species', 'species__species_id', 'species__synonyms', 'species__common_name_1', 'species__common_name_2', 'species__common_name_3', 'species__common_name_4', 'species__common_name_5', 'species__common_name_6', 'species__iucn_status', 'species__red_list_criteria', 'species__year_assessed', 'species__population_trend', 'species__coloniality', 'species__breeding_dist', 'species__nest_locations', 'species__hatchling_type', 'female_mass_mean', 'female_mass_upper', 'female_mass_lower', 'female_mass_uncertainty', 'male_mass_mean', 'male_mass_lower', 'male_mass_upper', 'male_mass_uncertainty', 'clutch_size_mean', 'clutch_size_lower', 'cluth_size_upper', 'clutch_size_uncertainty', 'clutch_interval', 'incubation_mean', 'incubation_period_lower', 'incubtaion_period_upper', 'incubation_period_uncertainty', 'fledging_period_mean', 'fledging_period_lower', 'fledging_period_upper', 'fledging_period_uncertainty', 'max_growth_mean', 'max_growth_lower', 'max_growth_upper', 'max_growth_uncertainty', 'post_fledge_care_mean', 'post_fledge_care_lower', 'post_fledge_care_upper', 'post_fledge_care_uncertainty', 'age_first_breed_mean', 'age_first_breed_lower', 'age_first_breed_upper', 'age_first_breed_uncertainty', 'foraging_distance', 'wingspan_mean', 'wingspan_lower', 'wingspan_upper', 'wingspan_uncertainty', 'max_age_mean', 'max_age_lower', 'max_age_upper', 'max_age_uncertainty', 'annual_survival_mean', 'annual_survival_lower', 'annual_survival_upper', 'annual_survival_uncertainty', 'citation', 'username', 'dt')
    
    return render_to_csv_response(all)

def downloadSpecies(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        all = Traits.objects.filter(species_id = l).values('species__fid', 'species__ord', 'species__fam', 'species__genus', 'species__species', 'species__species_id', 'species__synonyms', 'species__common_name_1', 'species__common_name_2', 'species__common_name_3', 'species__common_name_4', 'species__common_name_5', 'species__common_name_6', 'species__iucn_status', 'species__red_list_criteria', 'species__year_assessed', 'species__population_trend', 'species__coloniality', 'species__breeding_dist', 'species__nest_locations', 'species__hatchling_type', 'female_mass_mean', 'female_mass_upper', 'female_mass_lower', 'female_mass_uncertainty', 'male_mass_mean', 'male_mass_lower', 'male_mass_upper', 'male_mass_uncertainty', 'clutch_size_mean', 'clutch_size_lower', 'cluth_size_upper', 'clutch_size_uncertainty', 'clutch_interval', 'incubation_mean', 'incubation_period_lower', 'incubtaion_period_upper', 'incubation_period_uncertainty', 'fledging_period_mean', 'fledging_period_lower', 'fledging_period_upper', 'fledging_period_uncertainty', 'max_growth_mean', 'max_growth_lower', 'max_growth_upper', 'max_growth_uncertainty', 'post_fledge_care_mean', 'post_fledge_care_lower', 'post_fledge_care_upper', 'post_fledge_care_uncertainty', 'age_first_breed_mean', 'age_first_breed_lower', 'age_first_breed_upper', 'age_first_breed_uncertainty', 'foraging_distance', 'wingspan_mean', 'wingspan_lower', 'wingspan_upper', 'wingspan_uncertainty', 'max_age_mean', 'max_age_lower', 'max_age_upper', 'max_age_uncertainty', 'annual_survival_mean', 'annual_survival_lower', 'annual_survival_upper', 'annual_survival_uncertainty', 'citation', 'username', 'dt')
    
    return render_to_csv_response(all)

def downloadOrder(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        all = Traits.objects.filter(species__ord = l).values('species__fid', 'species__ord', 'species__fam', 'species__genus', 'species__species', 'species__species_id', 'species__synonyms', 'species__common_name_1', 'species__common_name_2', 'species__common_name_3', 'species__common_name_4', 'species__common_name_5', 'species__common_name_6', 'species__iucn_status', 'species__red_list_criteria', 'species__year_assessed', 'species__population_trend', 'species__coloniality', 'species__breeding_dist', 'species__nest_locations', 'species__hatchling_type', 'female_mass_mean', 'female_mass_upper', 'female_mass_lower', 'female_mass_uncertainty', 'male_mass_mean', 'male_mass_lower', 'male_mass_upper', 'male_mass_uncertainty', 'clutch_size_mean', 'clutch_size_lower', 'cluth_size_upper', 'clutch_size_uncertainty', 'clutch_interval', 'incubation_mean', 'incubation_period_lower', 'incubtaion_period_upper', 'incubation_period_uncertainty', 'fledging_period_mean', 'fledging_period_lower', 'fledging_period_upper', 'fledging_period_uncertainty', 'max_growth_mean', 'max_growth_lower', 'max_growth_upper', 'max_growth_uncertainty', 'post_fledge_care_mean', 'post_fledge_care_lower', 'post_fledge_care_upper', 'post_fledge_care_uncertainty', 'age_first_breed_mean', 'age_first_breed_lower', 'age_first_breed_upper', 'age_first_breed_uncertainty', 'foraging_distance', 'wingspan_mean', 'wingspan_lower', 'wingspan_upper', 'wingspan_uncertainty', 'max_age_mean', 'max_age_lower', 'max_age_upper', 'max_age_uncertainty', 'annual_survival_mean', 'annual_survival_lower', 'annual_survival_upper', 'annual_survival_uncertainty', 'citation', 'username', 'dt')
    
    return render_to_csv_response(all)

def downloadFamily(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')
        all = Traits.objects.filter(species__fam = l).values('species__fid', 'species__ord', 'species__fam', 'species__genus', 'species__species', 'species__species_id', 'species__synonyms', 'species__common_name_1', 'species__common_name_2', 'species__common_name_3', 'species__common_name_4', 'species__common_name_5', 'species__common_name_6', 'species__iucn_status', 'species__red_list_criteria', 'species__year_assessed', 'species__population_trend', 'species__coloniality', 'species__breeding_dist', 'species__nest_locations', 'species__hatchling_type', 'female_mass_mean', 'female_mass_upper', 'female_mass_lower', 'female_mass_uncertainty', 'male_mass_mean', 'male_mass_lower', 'male_mass_upper', 'male_mass_uncertainty', 'clutch_size_mean', 'clutch_size_lower', 'cluth_size_upper', 'clutch_size_uncertainty', 'clutch_interval', 'incubation_mean', 'incubation_period_lower', 'incubtaion_period_upper', 'incubation_period_uncertainty', 'fledging_period_mean', 'fledging_period_lower', 'fledging_period_upper', 'fledging_period_uncertainty', 'max_growth_mean', 'max_growth_lower', 'max_growth_upper', 'max_growth_uncertainty', 'post_fledge_care_mean', 'post_fledge_care_lower', 'post_fledge_care_upper', 'post_fledge_care_uncertainty', 'age_first_breed_mean', 'age_first_breed_lower', 'age_first_breed_upper', 'age_first_breed_uncertainty', 'foraging_distance', 'wingspan_mean', 'wingspan_lower', 'wingspan_upper', 'wingspan_uncertainty', 'max_age_mean', 'max_age_lower', 'max_age_upper', 'max_age_uncertainty', 'annual_survival_mean', 'annual_survival_lower', 'annual_survival_upper', 'annual_survival_uncertainty', 'citation', 'username', 'dt')
    
    return render_to_csv_response(all)



def dbsearch(request):
    SpeciesList = Species.objects.all().order_by('species_id')
    CnameList = Species.objects.all().order_by('common_name_1')
    X = Species.objects.all().distinct('ord').order_by('ord').values_list('ord')
    Y = Species.objects.all().distinct('fam').order_by('fam').values_list('fam')

    context = RequestContext(request, {'commonnames':CnameList,'species':SpeciesList,'orders':X,'families':Y})
    template = loader.get_template('app/dbsearch.html')        
    return HttpResponse(template.render(context))
        
    
def dbadd(request):
    SpeciesList = Species.objects.all().order_by('species_id')

    context = RequestContext(request, {'species':SpeciesList })
    template = loader.get_template('app/dbadd.html')        
    return HttpResponse(template.render(context))


def species(request):
    if request.method == 'GET':
        l = request.GET.get('l', '')        
        List = Species.objects.filter(species_id = l)
            
    context = RequestContext(request, {'LIST':List})
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


def gettraits(request):
    if request.method == 'GET':
        t = request.GET.get('t','')
        traits = Traits.objects.filter(species_id = t)

    context = RequestContext(request, {'TRAITS':traits})
    template = loader.get_template('app/searchresulttraits.html')        
    return HttpResponse(template.render(context))
