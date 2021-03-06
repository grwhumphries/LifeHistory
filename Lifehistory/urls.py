﻿"""
Definition of urls for Lifehistory.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^lifehistory$', 'app.views.lifehistory', name='lifehistory'),
    url(r'^dbsearch$','app.views.dbsearch',name='dbsearch'),
    url(r'^dbadd/','app.views.dbadd',name='dbadd'),
    url(r'^dbaddother/','app.views.dbaddother',name='dbaddother'),

    url(r'^species/','app.views.species',name='species'),
    url(r'^order/','app.views.order',name='order'),    
    url(r'^commonname/','app.views.commonname',name='commonname'),
    url(r'^family/','app.views.family',name='family'),
    url(r'^numerictraits/','app.views.numerictraits', name='numerictraits'),
    url(r'^charactertraits/','app.views.charactertraits', name='charactertraits'),

    #url(r'^downloadall$','app.views.downloadall',name='downloadall'),
    url(r'^downloadCommon/','app.views.downloadCommon',name='downloadCommon'),
    url(r'^downloadSpecies/','app.views.downloadSpecies',name='downloadSpecies'),
    url(r'^downloadOrder/','app.views.downloadOrder',name='downloadOrder'),
    url(r'^downloadFamily/','app.views.downloadFamily',name='downloadFamily'),
    url(r'^downloadALL/','app.views.downloadALL', name='downloadALL'),


    url(r'^EntryKey$','app.views.entrykey',name='entrykey'),    
    url(r'^dbPost$','app.views.dbPost',name='dbPost'),
    url(r'^dbPostother$','app.views.dbPostother',name='dbPostother'),

    url(r'^chartraits/', 'app.views.chartraits',name='chartraits'),

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
                'month':datetime.now().month,
                'day':datetime.now().day,
            }
        },
        name='login'),


    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),     
)
