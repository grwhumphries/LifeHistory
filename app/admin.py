from django.contrib import admin
from django.db import models
from app.models import Species, Traits


admin.site.register(Traits)
admin.site.register(Species)
