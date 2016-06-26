"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Species(models.Model):
    species_id = models.CharField(primary_key=True, max_length=30)
    order = models.CharField(blank=True, null=True, max_length=50)
    family = models.CharField(blank=True, null=True, max_length=50)
    genus = models.CharField(blank=True, null=True, max_length=50)
    species = models.CharField(blank=True, null=True, max_length=50)
    synonyms = models.CharField(blank=True, null=True, max_length=100)
    common_name_1 = models.CharField(blank=True, null=True, max_length=40)
    common_name_2 = models.CharField(blank=True, null=True, max_length=40)
    common_name_3 = models.CharField(blank=True, null=True, max_length=40)
    common_name_4 = models.CharField(blank=True, null=True, max_length=40)
    common_name_5 = models.CharField(blank=True, null=True, max_length=40)
    common_name_6 = models.CharField(blank=True, null=True, max_length=40)
    iucn_status = models.CharField(blank=True, null=True, max_length=50)
    red_list_criteria = models.CharField(blank=True, null=True, max_length=50)
    year_assessed = models.PositiveIntegerField(blank=True, null=True)
    population_trend = models.CharField(blank=True, null=True, max_length=50)
    coloniality = models.CharField(blank=True, null=True, max_length=15)
    breeding_dist = models.CharField(blank=True, null=True, max_length=15)
    nest_locations = models.CharField(blank=True, null=True, max_length=15)
    hatchling_type = models.CharField(blank=True, null=True, max_length=15)

    def __unicode__(self):
        return self.species_id


    class Meta:
        db_table = 'species'
        verbose_name = "Species"
        verbose_name_plural = "Species"


class Traits(models.Model):
    feature_id = models.AutoField(primary_key=True)
    spec = models.ForeignKey('Species',blank=True,null=True)
   
    female_mass_mean = models.CharField(blank=True, null=True, max_length=5)
    female_mass_upper = models.CharField(blank=True, null=True, max_length=5)
    female_mass_lower = models.CharField(blank=True, null=True, max_length=5)
    female_mass_uncertainty = models.CharField(blank=True, null=True, max_length=10)

    male_mass_mean = models.CharField(blank=True, null=True, max_length=5)
    male_mass_upper = models.CharField(blank=True, null=True, max_length=5)
    male_mass_lower = models.CharField(blank=True, null=True, max_length=5)
    male_mass_uncertainty = models.CharField(blank=True, null=True, max_length=10)    
    
    clutch_size_mean = models.CharField(blank=True, null=True, max_length=5)
    clutch_size_upper = models.CharField(blank=True, null=True, max_length=5)
    clutch_size_lower = models.CharField(blank=True, null=True, max_length=5)
    clutch_size_uncertainty = models.CharField(blank=True, null=True, max_length=10)
    clutch_interval = models.CharField(blank=True, null=True, max_length=15)

    
    incubation_period_mean = models.CharField(blank=True, null=True, max_length=5)
    incubation_period_upper = models.CharField(blank=True, null=True, max_length=5)
    incubation_period_lower = models.CharField(blank=True, null=True, max_length=5)
    incubation_period_uncertainty = models.CharField(blank=True,null=True, max_length=10)


    fledgling_period_mean = models.CharField(blank=True, null=True, max_length=5)
    fledgling_period_upper = models.CharField(blank=True, null=True, max_length=5)
    fledgling_period_lower = models.CharField(blank=True, null=True, max_length=5)
    fledgling_period_uncertainty = models.CharField(blank=True, null=True, max_length=10)


    max_growth_rate_mean = models.CharField(blank=True, null=True, max_length=5)
    max_growth_rate_upper = models.CharField(blank=True, null=True, max_length=5)
    max_growth_rate_lower = models.CharField(blank=True, null=True, max_length=5)
    max_growth_rate_uncertainty = models.CharField(blank=True, null = True, max_length=10)

    post_fledging_care_mean = models.CharField(blank=True, null=True, max_length=5)
    post_fledging_care_upper = models.CharField(blank=True, null=True, max_length=5)
    post_fledging_care_lower = models.CharField(blank=True, null=True, max_length=5)
    post_fledging_care_uncertainty = models.CharField(blank=True,null=True, max_length=10)
    
    age_first_breeding_mean = models.IntegerField(blank=True, null=True)
    age_first_breeding_upper = models.IntegerField(blank=True, null=True)
    age_first_breeding_lower = models.IntegerField(blank=True, null=True)
    age_first_breeding_uncertainty = models.CharField(blank=True, null=True, max_length=10)

    foraging_distance = models.CharField(blank=True, null=True, max_length=15)

    wingspan_mean = models.CharField(blank=True, null=True, max_length=5)
    wingspan_upper = models.CharField(blank=True, null=True, max_length=5)
    wingspan_lower = models.CharField(blank=True, null=True, max_length=5)
    wingspan_uncertainty = models.CharField(blank=True, null=True, max_length=10)
    
    max_age_mean = models.CharField(blank=True, null=True, max_length=5)
    max_age_upper = models.CharField(blank=True, null=True, max_length=5)
    max_age_lower = models.CharField(blank=True, null=True, max_length=5)
    max_age_uncertainty = models.CharField(blank=True, null=True, max_length=10)

    annual_survival_mean = models.CharField(blank=True, null=True, max_length=5)
    annual_survival_upper = models.CharField(blank=True, null=True, max_length=5)
    annual_survival_lower = models.CharField(blank=True, null=True, max_length=5)
    annual_survival_uncertainty = models.CharField(blank=True, null=True, max_length=10)

    citation = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.feature_id


    class Meta:
        db_table = 'traits'
        verbose_name = "Traits"
        verbose_name_plural = "Traits"
