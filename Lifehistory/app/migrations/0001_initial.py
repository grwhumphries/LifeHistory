# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('species_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('order', models.CharField(max_length=50, null=True, blank=True)),
                ('family', models.CharField(max_length=50, null=True, blank=True)),
                ('genus', models.CharField(max_length=50, null=True, blank=True)),
                ('species', models.CharField(max_length=50, null=True, blank=True)),
                ('synonyms', models.CharField(max_length=100, null=True, blank=True)),
                ('common_names', models.CharField(max_length=100, null=True, blank=True)),
                ('iucn_status', models.CharField(max_length=50, null=True, blank=True)),
                ('red_list_criteria', models.CharField(max_length=50, null=True, blank=True)),
                ('year_assessed', models.PositiveIntegerField(null=True, blank=True)),
                ('population_trend', models.CharField(max_length=50, null=True, blank=True)),
                ('coloniality', models.CharField(max_length=15, null=True, blank=True)),
                ('breeding_dist', models.CharField(max_length=15, null=True, blank=True)),
                ('nest_locations', models.CharField(max_length=15, null=True, blank=True)),
                ('hatchling_type', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'db_table': 'species',
                'verbose_name': 'Species',
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Traits',
            fields=[
                ('feature_id', models.AutoField(serialize=False, primary_key=True)),
                ('female_mass_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('female_mass_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('female_mass_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('female_mass_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('male_mass_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('male_mass_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('male_mass_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('male_mass_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('clutch_size_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('clutch_size_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('clutch_size_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('clutch_size_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('clutch_interval', models.CharField(max_length=15, null=True, blank=True)),
                ('incubation_period_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('incubation_period_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('incubation_period_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('incubation_period_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('fledgling_period_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('fledgling_period_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('fledgling_period_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('fledgling_period_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('max_growth_rate_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('max_growth_rate_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('max_growth_rate_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('max_growth_rate_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('post_fledging_care_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('post_fledging_care_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('post_fledging_care_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('post_fledging_care_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('age_first_breeding_mean', models.IntegerField(null=True, blank=True)),
                ('age_first_breeding_upper', models.IntegerField(null=True, blank=True)),
                ('age_first_breeding_lower', models.IntegerField(null=True, blank=True)),
                ('age_first_breeding_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('foraging_distance', models.CharField(max_length=15, null=True, blank=True)),
                ('wingspan_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('wingspan_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('wingspan_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('wingspan_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('max_age_mean', models.IntegerField(null=True, blank=True)),
                ('max_age_upper', models.IntegerField(null=True, blank=True)),
                ('max_age_lower', models.IntegerField(null=True, blank=True)),
                ('max_age_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('annual_survival_mean', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('annual_survival_upper', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('annual_survival_lower', models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)),
                ('annual_survival_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('citation', models.TextField(null=True, blank=True)),
                ('species', models.ForeignKey(db_column=b'species_id', blank=True, to='app.Species', null=True)),
            ],
            options={
                'db_table': 'traits',
                'verbose_name': 'Traits',
                'verbose_name_plural': 'Traits',
            },
        ),
    ]
