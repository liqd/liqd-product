# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adhocracy4.maps.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('meinberlin_maps', '0001_initial')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapPreset',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('polygon', adhocracy4.maps.fields.MultiPolygonField()),
            ],
            options={
                'db_table': 'meinberlin_maps_mappreset',
            },
        ),
        migrations.CreateModel(
            name='MapPresetCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'meinberlin_maps_mappresetcategory',
            },
        ),
        migrations.AddField(
            model_name='mappreset',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='a4_candy_maps.MapPresetCategory', null=True),
        ),
    ]
