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
    genus_species = models.CharField(max_length=40, blank=True, null=True)
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
    species = models.ForeignKey(Species, db_column='species_id')
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
    clutch_size_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    clutch_size_uncertainty = models.CharField(max_length=50, blank=True, null=True)
    clutch_interval = models.CharField(max_length=50, blank=True, null=True)
    incubation_mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    incubation_period_lower = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    incubation_period_upper = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
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
    mate_fidelity = models.CharField(max_length=5, blank=True, null=True)
    site_fidelity = models.CharField(max_length=5, blank=True, null=True)
    coloniality = models.CharField(max_length=5, blank=True, null=True)
    citation = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BreedingDistributions(models.Model):
    brid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    breeding_distribution_id = models.IntegerField()
    breeding_distribution = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'breeding_distributions'


class Citation(models.Model):
    cite_id = models.CharField(primary_key=True, max_length=15)
    citation_name = models.CharField(max_length=100)
    citation = models.CharField(max_length=2000)

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class IucnData(models.Model):
    iucnid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    iucn_status = models.CharField(max_length=4, blank=True, null=True)
    red_list_criteria = models.CharField(max_length=100, blank=True, null=True)
    year_assessed = models.IntegerField(blank=True, null=True)
    population_trend = models.CharField(max_length=60, blank=True, null=True)
    population_estimate = models.IntegerField(blank=True, null=True)
    population_range = models.TextField(blank=True, null=True)  # This field type is a guess.
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

    class Meta:
        managed = False
        db_table = 'nest_locations'


class NumericTraits(models.Model):
    feature_id = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    traits = models.CharField(max_length=60)
    mean = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    range = models.TextField(blank=True, null=True)  # This field type is a guess.
    uncertainty = models.CharField(max_length=10, blank=True, null=True)
    units = models.CharField(max_length=20)
    comments = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'numeric_traits'

    def __unicode__(self):
        return self.species_id

    class Meta:
        db_table = 'traits'
        verbose_name = "Traits"
        verbose_name_plural = "Traits"


class OtherTraits(models.Model):
    trtid = models.IntegerField(primary_key=True)
    species = models.ForeignKey('Species')
    variable = models.CharField(max_length=40)
    value = models.CharField(max_length=40, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=30)
    dt = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'other_traits'


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