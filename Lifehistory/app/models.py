"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Species(models.Model):
    fid = models.SmallIntegerField()
    ord = models.CharField(max_length=20, blank=True, null=True)
    fam = models.CharField(max_length=20, blank=True, null=True)
    genus = models.CharField(max_length=20)
    species = models.CharField(max_length=20, blank=True, null=True)
    species_id = models.CharField(primary_key=True, max_length=40)
    synonyms = models.CharField(max_length=300, blank=True, null=True)
    common_name_1 = models.CharField(max_length=40)
    common_name_2 = models.CharField(max_length=50, blank=True, null=True)
    common_name_3 = models.CharField(max_length=50, blank=True, null=True)
    common_name_4 = models.CharField(max_length=50, blank=True, null=True)
    common_name_5 = models.CharField(max_length=50, blank=True, null=True)
    common_name_6 = models.CharField(max_length=50, blank=True, null=True)
    iucn_status = models.CharField(max_length=4, blank=True, null=True)
    red_list_criteria = models.CharField(max_length=100, blank=True, null=True)
    year_assessed = models.IntegerField(blank=True, null=True)
    population_trend = models.CharField(max_length=20, blank=True, null=True)
    coloniality = models.CharField(max_length=5, blank=True, null=True)
    breeding_dist = models.CharField(max_length=10, blank=True, null=True)
    nest_locations = models.CharField(max_length=15, blank=True, null=True)
    hatchling_type = models.CharField(max_length=5, blank=True, null=True)

    def __unicode__(self):
        return self.species_id

    class Meta:
        db_table = 'species'
        verbose_name = "Species"
        verbose_name_plural = "Species"


class Traits(models.Model):
    feature_id = models.SmallIntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    female_mass_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    female_mass_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    female_mass_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    female_mass_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    male_mass_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    male_mass_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    male_mass_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    male_mass_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    clutch_size_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    clutch_size_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cluth_size_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    clutch_size_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    clutch_interval = models.CharField(max_length=50, blank=True, null=True)
    incubation_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    incubation_period_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    incubtaion_period_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    incubation_period_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    fledging_period_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    fledging_period_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    fledging_period_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    fledging_period_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    max_growth_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_growth_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_growth_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_growth_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    post_fledge_care_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    post_fledge_care_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    post_fledge_care_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    post_fledge_care_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    age_first_breed_mean = models.CharField(max_length=10, blank=True, null=True)
    age_first_breed_lower = models.IntegerField(blank=True, null=True)
    age_first_breed_upper = models.IntegerField(blank=True, null=True)
    age_first_breed_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    foraging_distance = models.CharField(max_length=50, blank=True, null=True)
    wingspan_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    wingspan_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    wingspan_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    wingspan_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    max_age_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    max_age_lower = models.IntegerField(blank=True, null=True)
    max_age_upper = models.IntegerField(blank=True, null=True)
    max_age_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    annual_survival_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    annual_survival_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    annual_survival_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    annual_survival_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    citation = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)



    class Meta:
        db_table = 'traits'
        verbose_name = "Traits"
        verbose_name_plural = "Traits"