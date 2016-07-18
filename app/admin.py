from django.contrib import admin
from django.db import models
from app.models import Species, NumericTraits


admin.site.register(NumericTraits)
admin.site.register(Species)
