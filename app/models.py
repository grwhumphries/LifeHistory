
"""
Definition of models.
"""

from django.db import models

from django.contrib.postgres.fields.ranges import FloatRangeField

# Create your models here.
 
class Species(models.Model):
    ord = models.CharField(max_length=20)
    fam = models.CharField(max_length=20)
    genus = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    subspecies = models.CharField(max_length=50, blank=True, null=True)
    species_id = models.CharField(primary_key=True, max_length=40)
    species_id_html = models.CharField(max_length=40)
    synonyms = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.species_id

    class Meta:
        managed = False
        db_table = 'species'
        verbose_name = "Species"
        verbose_name_plural = "Species"



def citation_id_create():
    X = len(Citation.objects.all().values_list())
    return 'citation'+str(X+1)

class Citation(models.Model):
    cite_id = models.CharField(primary_key=True, max_length=25, default=citation_id_create)
    citation_name = models.CharField(max_length=100)
    citation = models.TextField()

    def __unicode__(self):
        return self.citation_name

    class Meta:
        managed = False
        db_table = 'citation'
        ordering = ['citation_name']



class NumericTraits(models.Model):
    feature_id = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    traits = models.CharField(max_length=30)
    mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    range = FloatRangeField (blank=True, null=True)  
    uncertainty = models.CharField(max_length=10, blank=True, null=True)
    units = models.CharField(max_length=20)
    comments = models.TextField(blank=True, null=True)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    def __unicode__(self):
        return self.species_id + " | " + self.traits + " | " + self.cite_id

    class Meta:
        db_table = 'numeric_traits'
        verbose_name = "Numeric Traits"
        verbose_name_plural = "Numeric Traits"
        ordering = ['traits']


class OtherTraits(models.Model):
    trt_id = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    variable = models.CharField(max_length=40)
    value = models.CharField(max_length=40, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.trt_id) + " | " + self.species_id


    class Meta:
        managed = False
        db_table = 'other_traits'
        verbose_name = "Character Traits"
        verbose_name_plural = "Character Traits"
        ordering = ['variable']


class BreedingDistributions(models.Model):
    brid = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    breeding_distribution_id = models.IntegerField()
    breeding_distribution = models.CharField(max_length = 5)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    def __unicode__(self):
        return self.species_id + " | " + self.breeding_distribution

    class Meta:
        managed = False
        db_table = 'breeding_distributions'
        verbose_name = "Breeding distribution"
        verbose_name_plural = "Breeding distribution"






class CitationNumerictraitSpecies(models.Model):
    relation_id = models.IntegerField(primary_key=True)
    feature = models.ForeignKey(NumericTraits)
    cite = models.ForeignKey(Citation)
    species = models.ForeignKey(Species)

    def __unicode__(self):
        return self.species_id + " | " + self.cite_id + " | " + str(self.feature_id)


    class Meta:
        managed = False
        db_table = 'citation_numerictrait_species'
        verbose_name = "Citation numerictrait table"
        verbose_name_plural = "Citation numerictrait table"

class CitationOthertraitSpecies(models.Model):
    relation_id = models.IntegerField(primary_key=True)
    trt = models.ForeignKey(OtherTraits, db_column='trt_id')
    cite = models.ForeignKey(Citation)
    species = models.ForeignKey(Species)

    def __unicode__(self):
        return self.species_id + " | " + self.cite_id + " | " + str(self.trt_id) 


    class Meta:
        managed = False
        db_table = 'citation_othertrait_species'
        verbose_name = "Citation othertrait table"
        verbose_name_plural = "Citation othertrait table"        


class CommonNames(models.Model):
    cnid = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    common_name_id = models.IntegerField()
    common_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.species_id + " | " + self.common_name


    class Meta:
        managed = False
        db_table = 'common_names'
        verbose_name = "Common names"
        verbose_name_plural = "Common names"
        ordering = ['species_id','common_name']


class Foraging(models.Model):
    forid = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    value = models.CharField(max_length=10)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    def __unicode__(self):
        return self.species_id + " | " + self.value

    class Meta:
        managed = False
        db_table = 'foraging'
        verbose_name = 'Foraging location'
        verbose_name_plural = 'Foraging location'

class IucnData(models.Model):
    iucnid = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    iucn_status = models.CharField(max_length=4, blank=True, null=True)
    red_list_criteria = models.CharField(max_length=100, blank=True, null=True)
    year_assessed = models.IntegerField(blank=True, null=True)
    population_trend = models.CharField(max_length=60, blank=True, null=True)
    population_estimate = models.IntegerField(blank=True, null=True)
    population_range = FloatRangeField(blank=True, null=True)  
    population_uncertainty = models.CharField(max_length=10, blank=True, null=True)
    population_location = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.species_id + " | " + self.year_assessed

    class Meta:
        managed = False
        db_table = 'iucn_data'
        verbose_name = 'IUCN data'
        verbose_name_plural = 'IUCN data'

class NestLocations(models.Model):
    nlid = models.IntegerField(primary_key=True)
    species = models.ForeignKey(Species)
    nest_location_id = models.IntegerField()
    nest_location = models.CharField(max_length=10)
    cite = models.ForeignKey(Citation)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    def __unicode__(self):
        return self.species_id + " | " + self.nest_location

    class Meta:
        managed = False
        db_table = 'nest_locations'
        verbose_name = "Nesting locations"
        verbose_name_plural = "Nesting locations"






class Traitnames(models.Model):
    trtnmid = models.IntegerField(primary_key=True)
    tble = models.CharField(max_length=40)
    variable = models.CharField(max_length=40)
    tr_value = models.CharField(max_length=25)
    tr_name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.variable + " | " + self.tr_name

    class Meta:
        managed = False
        db_table = 'traitnames'
        verbose_name = "Trait values"
        verbose_name_plural = "Trait values"
