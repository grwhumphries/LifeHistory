# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traits',
            name='species',
        ),
        migrations.AddField(
            model_name='traits',
            name='spec_id',
            field=models.ForeignKey(blank=True, to='app.Species', null=True),
        ),
    ]
