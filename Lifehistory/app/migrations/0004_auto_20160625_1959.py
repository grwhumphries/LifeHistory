# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160625_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traits',
            name='female_mass_lower',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='traits',
            name='female_mass_upper',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
