# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160625_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traits',
            old_name='spec_id',
            new_name='species_id',
        ),
    ]
