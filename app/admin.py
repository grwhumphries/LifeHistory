from django.contrib import admin
from django.db import models
from app.models import *



class NumericAdmin(admin.ModelAdmin):
    search_fields = ('species__species_id',)    

class OtherAdmin(admin.ModelAdmin):
    search_fields = ('species__species_id',)


admin.site.register(NumericTraits, NumericAdmin)
admin.site.register(OtherTraits, OtherAdmin)
admin.site.register(Species)
admin.site.register(Citation)
admin.site.register(CommonNames)
admin.site.register(IucnData)
admin.site.register(Traitnames)
admin.site.register(NestLocations)
admin.site.register(BreedingDistributions)
admin.site.register(Foraging)
admin.site.register(CitationNumerictraitSpecies)
admin.site.register(CitationOthertraitSpecies)
