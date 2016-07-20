from django.contrib import admin
from django.db import models
from app.models import *


admin.site.register(NumericTraits)
admin.site.register(OtherTraits)
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
