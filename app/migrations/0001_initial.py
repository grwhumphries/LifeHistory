# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BreedingDistributions',
            fields=[
                ('brid', models.IntegerField(serialize=False, primary_key=True)),
                ('breeding_distribution_id', models.IntegerField()),
                ('breeding_distribution', models.CharField(max_length=5)),
                ('username', models.CharField(max_length=30)),
                ('dt', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Breeding distribution',
                'db_table': 'breeding_distributions',
                'managed': False,
                'verbose_name_plural': 'Breeding distribution',
            },
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('cite_id', models.CharField(default=app.models.citation_id_create, max_length=25, serialize=False, primary_key=True)),
                ('citation_name', models.CharField(max_length=100)),
                ('citation', models.TextField()),
            ],
            options={
                'ordering': ['citation_name'],
                'db_table': 'citation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CitationNumerictraitSpecies',
            fields=[
                ('relation_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name': 'Citation numerictrait table',
                'db_table': 'citation_numerictraits_species',
                'managed': False,
                'verbose_name_plural': 'Citation numerictrait table',
            },
        ),
        migrations.CreateModel(
            name='CitationOthertraitSpecies',
            fields=[
                ('relation_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name': 'Citation othertrait table',
                'db_table': 'citation_othertraits_species',
                'managed': False,
                'verbose_name_plural': 'Citation othertrait table',
            },
        ),
        migrations.CreateModel(
            name='CommonNames',
            fields=[
                ('cnid', models.IntegerField(serialize=False, primary_key=True)),
                ('common_name_id', models.IntegerField()),
                ('common_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['species_id', 'common_name'],
                'verbose_name': 'Common names',
                'db_table': 'common_names',
                'managed': False,
                'verbose_name_plural': 'Common names',
            },
        ),
        migrations.CreateModel(
            name='Foraging',
            fields=[
                ('forid', models.IntegerField(serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=30)),
                ('dt', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Foraging location',
                'db_table': 'foraging',
                'managed': False,
                'verbose_name_plural': 'Foraging location',
            },
        ),
        migrations.CreateModel(
            name='IucnData',
            fields=[
                ('iucnid', models.IntegerField(serialize=False, primary_key=True)),
                ('iucn_status', models.CharField(max_length=4, null=True, blank=True)),
                ('red_list_criteria', models.CharField(max_length=100, null=True, blank=True)),
                ('year_assessed', models.IntegerField(null=True, blank=True)),
                ('population_trend', models.CharField(max_length=60, null=True, blank=True)),
                ('population_estimate', models.IntegerField(null=True, blank=True)),
                ('population_range', django.contrib.postgres.fields.ranges.FloatRangeField(null=True, blank=True)),
                ('population_uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('population_location', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'IUCN data',
                'db_table': 'iucn_data',
                'managed': False,
                'verbose_name_plural': 'IUCN data',
            },
        ),
        migrations.CreateModel(
            name='NestLocations',
            fields=[
                ('nlid', models.IntegerField(serialize=False, primary_key=True)),
                ('nest_location_id', models.IntegerField()),
                ('nest_location', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=30)),
                ('dt', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Nesting locations',
                'db_table': 'nest_locations',
                'managed': False,
                'verbose_name_plural': 'Nesting locations',
            },
        ),
        migrations.CreateModel(
            name='OtherTraits',
            fields=[
                ('trt_id', models.IntegerField(serialize=False, primary_key=True)),
                ('variable', models.CharField(max_length=40)),
                ('value', models.CharField(max_length=40, null=True, blank=True)),
                ('comments', models.TextField(null=True, blank=True)),
                ('study_year', models.CharField(max_length=300, null=True, blank=True)),
                ('study_location', models.CharField(max_length=300, null=True, blank=True)),
                ('username', models.CharField(max_length=30)),
                ('dt', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Character Traits',
                'db_table': 'other_traits',
                'managed': False,
                'verbose_name_plural': 'Character Traits',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('ord', models.CharField(max_length=20)),
                ('fam', models.CharField(max_length=20)),
                ('genus', models.CharField(max_length=20)),
                ('species', models.CharField(max_length=20)),
                ('subspecies', models.CharField(max_length=50, null=True, blank=True)),
                ('species_id', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('species_id_html', models.CharField(max_length=40)),
                ('synonyms', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Species',
                'db_table': 'species',
                'managed': False,
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Traitnames',
            fields=[
                ('trtnmid', models.IntegerField(serialize=False, primary_key=True)),
                ('tble', models.CharField(max_length=40)),
                ('variable', models.CharField(max_length=40)),
                ('tr_value', models.CharField(max_length=25)),
                ('tr_name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Trait values',
                'db_table': 'traitnames',
                'managed': False,
                'verbose_name_plural': 'Trait values',
            },
        ),
        migrations.CreateModel(
            name='NumericTraits',
            fields=[
                ('feature_id', models.IntegerField(serialize=False, primary_key=True)),
                ('traits', models.CharField(max_length=30)),
                ('mean', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('range', django.contrib.postgres.fields.ranges.FloatRangeField(null=True, blank=True)),
                ('uncertainty', models.CharField(max_length=10, null=True, blank=True)),
                ('units', models.CharField(max_length=20)),
                ('comments', models.TextField(null=True, blank=True)),
                ('study_year', models.CharField(max_length=300, null=True, blank=True)),
                ('study_location', models.CharField(max_length=300, null=True, blank=True)),
                ('username', models.CharField(max_length=30)),
                ('dt', models.CharField(max_length=30)),
                ('cite', models.ForeignKey(to='app.Citation')),
                ('species', models.ForeignKey(to='app.Species')),
            ],
            options={
                'db_table': 'numeric_traits',
                'verbose_name': 'Numeric Traits',
                'verbose_name_plural': 'Numeric Traits',
            },
        ),
    ]
