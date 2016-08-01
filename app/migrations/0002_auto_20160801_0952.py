# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='citationnumerictraitspecies',
            table='citation_numerictraits_species',
        ),
        migrations.AlterModelTable(
            name='citationothertraitspecies',
            table='citation_othertraits_species',
        ),
    ]
