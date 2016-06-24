"""
Definition of models.
"""

from django.db import models

# Create your models here.


class Species(models.Model):
    species_id = models.TextField(primary_key=True, db_column='species_id')
    feature_id = models.ForeignKey('Traits',db_column='feature_id',blank=True,null=True)
    order = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    common_names = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.species_id

    class Meta:
        managed = False
        db_table = 'species'
        verbose_name = "Species"
        verbose_name_plural = "Species"


class Traits(models.Model):
    feature_id = models.AutoField(primary_key=True)
    species_id = models.ForeignKey('Species',db_column='species_id',blank=True,null=True)
    iucn_status = models.TextField(blank=True, null=True)
    red_list_criteria = models.TextField(blank=True, null=True)
    year_assessed = models.TextField(blank=True, null=True)
    population_trend = models.TextField(blank=True, null=True)
    female_mass_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    female_mass_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    female_mass_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    female_mass_uncertainty = models.TextField(blank=True, null=True)

    male_mass_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    male_mass_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    male_mass_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    male_mass_uncertainty = models.TextField(blank=True, null=True)

    breeding_dist = models.TextField(blank=True, null=True)
    nest_locations = models.TextField(blank=True, null=True)
    
    clutch_size_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    clutch_size_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    clutch_size_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    clutch_size_uncertainty = models.TextField(blank=True, null=True)
    clutch_interval = models.TextField(blank=True, null=True)

    hatchling_type = models.TextField(blank=True, null=True)
    incubation_period_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    incubation_period_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    incubation_period_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    incubation_period_uncertainty = models.TextField(blank=True,null=True)


    fledgling_period_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fledgling_period_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fledgling_period_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fledgling_period_uncertainty = models.TextField(blank=True, null=True)


    max_growth_rate_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    max_growth_rate_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    max_growth_rate_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    max_growth_rate_uncertainty = models.TextField(blank=True, null = True)

    post_fledging_care_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    post_fledging_care_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    post_fledging_care_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    post_fledging_care_uncertainty = models.TextField(blank=True,null=True)
    
    age_first_breeding_mean = models.IntegerField(blank=True, null=True)
    age_first_breeding_upper = models.IntegerField(blank=True, null=True)
    age_first_breeding_lower = models.IntegerField(blank=True, null=True)
    age_first_breeding_uncertainty = models.TextField(blank=True, null=True)

    foraging_distance = models.TextField(blank=True, null=True)

    wingspan_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wingspan_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wingspan_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wingspan_uncertainty = models.TextField(blank=True, null=True)
    
    max_age_mean = models.IntegerField(blank=True, null=True)
    max_age_upper = models.IntegerField(blank=True, null=True)
    max_age_lower = models.IntegerField(blank=True, null=True)
    max_age_uncertainty = models.TextField(blank=True, null=True)

    annual_survival_mean = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    annual_survival_upper = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    annual_survival_lower = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    annual_survival_uncertainty = models.TextField(blank=True, null=True)

    coloniality = models.TextField(blank=True, null=True)

    citation = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return self.feature_id


    class Meta:
        managed = False
        db_table = 'species'
        verbose_name = "Species"
        verbose_name_plural = "Species"