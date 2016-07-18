
"""
Definition of models.
"""

from django.db import models

from django.contrib.postgres.fields.ranges import FloatRangeField

# Create your models here.
 

class BreedingDistributions(models.Model):
    brid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    breeding_distribution_id = models.IntegerField()
    breeding_distribution = models.CharField(max_length=10)
    cite = models.ForeignKey('Citation')
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'breeding_distributions'


class Citation(models.Model):
    cite_id = models.CharField(primary_key=True, max_length=15)
    citation_name = models.CharField(max_length=100)
    citation = models.TextField()

    class Meta:
        managed = False
        db_table = 'citation'


class CitationNumerictraits(models.Model):
    relation_id = models.IntegerField(primary_key=True)
    feature = models.ForeignKey('NumericTraits')
    cite = models.ForeignKey(Citation)

    class Meta:
        managed = False
        db_table = 'citation_numerictraits'


class CitationOthertraits(models.Model):
    relation_id = models.IntegerField(primary_key=True)
    trtid = models.ForeignKey('OtherTraits', db_column='trtid')
    cite = models.ForeignKey(Citation)

    class Meta:
        managed = False
        db_table = 'citation_othertraits'


class CommonNames(models.Model):
    cnid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    common_name_id = models.IntegerField()
    common_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'common_names'



class Foraging(models.Model):
    forid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    value = models.CharField(max_length=10)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'foraging'


class IucnData(models.Model):
    iucnid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    iucn_status = models.CharField(max_length=4, blank=True, null=True)
    red_list_criteria = models.CharField(max_length=100, blank=True, null=True)
    year_assessed = models.IntegerField(blank=True, null=True)
    population_trend = models.CharField(max_length=60, blank=True, null=True)
    population_estimate = models.IntegerField(blank=True, null=True)
    population_range = FloatRangeField(blank=True, null=True)  
    population_uncertainty = models.CharField(max_length=10, blank=True, null=True)
    population_location = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iucn_data'


class NestLocations(models.Model):
    nlid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    nest_location_id = models.IntegerField()
    nest_location = models.CharField(max_length=10)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'nest_locations'


class NumericTraits(models.Model):
    feature_id = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    traits = models.CharField(max_length=60)
    mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    range = FloatRangeField (blank=True, null=True)  
    uncertainty = models.CharField(max_length=10, blank=True, null=True)
    units = models.CharField(max_length=20)
    comments = models.TextField(blank=True, null=True)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    def __unicode__(self):
        return self.species_id

    class Meta:
        db_table = 'numeric_traits'
        verbose_name = "Numeric Traits"
        verbose_name_plural = "Numeric Traits"


class OtherTraits(models.Model):
    trtid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    variable = models.CharField(max_length=40)
    value = models.CharField(max_length=40, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    def __unicode__(self):
        return self.species_id


    class Meta:
        managed = False
        db_table = 'other_traits'
        verbose_name = "Character Traits"
        verbose_name_plural = "Character Traits"



class Species(models.Model):
    ord = models.CharField(max_length=20)
    fam = models.CharField(max_length=20)
    genus = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    subspecies = models.CharField(max_length=50, blank=True, null=True)
    species_id = models.CharField(primary_key=True, max_length=40)
    species_id_html = models.CharField(max_length=40)
    synonyms = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'species'


class SpeciesCitation(models.Model):
    relation_id = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    cite = models.ForeignKey(Citation)

    class Meta:
        managed = False
        db_table = 'species_citation'


class Traitnames(models.Model):
    trtnmid = models.IntegerField(primary_key=True)
    tble = models.CharField(max_length=40)
    variable = models.CharField(max_length=40)
    tr_value = models.CharField(max_length=15)
    tr_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'traitnames'

