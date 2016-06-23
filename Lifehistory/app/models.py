"""
Definition of models.
"""

from django.db import models

# Create your models here.


class Species(models.Model):
    species_id = models.AutoField(primary_key=True)
    feature_id = models.ForeignKey('Traits',db_column='feature_id',blank=True,null=True)
    order = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    common_name = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.genus+" "+self.species


    class Meta:
        managed = False
        db_table = 'species'
        verbose_name = "Species"
        verbose_name_plural = "Species"

class Traits(models.Model):
    feature_id = models.AutoField(primary_key=True)
    species_id = models.ForeignKey('Species',db_column='species_id',blank=True,null=True)
    iucn_status = models.TextField(blank=True, null=True)
    redlist_criteria = models.TextField(blank=True, null=True)
    year_assessed = models.TextField(blank=True, null=True)
    population_trend = models.TextField(blank=True, null=True)
    female_mass_mean = models.IntegerField(blank=True, null=True)
    female_mass_upper = models.IntegerField(blank=True, null=True)
    female_mass_lower = models.IntegerField(blank=True, null=True)
    male_mass_mean = models.IntegerField(blank=True, null=True)
    male_mass_upper = models.IntegerField(blank=True, null=True)
    male_mass_lower = models.IntegerField(blank=True, null=True)
    breeding_dist = models.TextField(blank=True, null=True)
    nesting_type = models.TextField(blank=True, null=True)
    clutch_size_mean = models.IntegerField(blank=True, null=True)
    clutch_size_upper = models.IntegerField(blank=True, null=True)
    clutch_size_lower = models.IntegerField(blank=True, null=True)
    hatchling_type = models.TextField(blank=True, null=True)
    incubation_period_mean = models.IntegerField(blank=True, null=True)
    incubation_period_upper = models.IntegerField(blank=True, null=True)
    incubation_period_lower = models.IntegerField(blank=True, null=True)
    fledgling_period_mean = models.IntegerField(blank=True, null=True)
    fledgling_period_upper = models.IntegerField(blank=True, null=True)
    fledgling_period_lower = models.IntegerField(blank=True, null=True)
    max_growth_rate_mean = models.IntegerField(blank=True, null=True)
    max_growth_rate_upper = models.IntegerField(blank=True, null=True)
    max_growth_rate_lower = models.IntegerField(blank=True, null=True)
    post_fledging_care = models.TextField(blank=True, null=True)
    age_first_breeding_mean = models.IntegerField(blank=True, null=True)
    age_first_breeding_upper = models.IntegerField(blank=True, null=True)
    age_first_breeding_lower = models.IntegerField(blank=True, null=True)
    foraging_distance = models.TextField(blank=True, null=True)
    wing_span_mean = models.IntegerField(blank=True, null=True)
    wing_span_upper = models.IntegerField(blank=True, null=True)
    wing_span_lower = models.IntegerField(blank=True, null=True)
    max_age_mean = models.IntegerField(blank=True, null=True)
    max_age_upper = models.IntegerField(blank=True, null=True)
    max_age_lower = models.IntegerField(blank=True, null=True)
    annual_survival_mean = models.IntegerField(blank=True, null=True)
    annual_survival_upper = models.IntegerField(blank=True, null=True)
    annual_survival_lower = models.IntegerField(blank=True, null=True)
    coloniality = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.feature_id


    class Meta:
        managed = False
        db_table = 'species'
        verbose_name = "Species"
        verbose_name_plural = "Species"