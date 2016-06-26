# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160625_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='common_names',
        ),
        migrations.AddField(
            model_name='species',
            name='common_name_1',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='species',
            name='common_name_2',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='species',
            name='common_name_3',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='species',
            name='common_name_4',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='species',
            name='common_name_5',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='species',
            name='common_name_6',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
