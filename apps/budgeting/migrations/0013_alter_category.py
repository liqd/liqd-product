# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 15:37
from __future__ import unicode_literals

import adhocracy4.categories.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('meinberlin_budgeting', '0013_alter_category')]

    dependencies = [
        ('a4_candy_budgeting', '0012_name_verbose_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='category',
            field=adhocracy4.categories.fields.CategoryField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4categories.Category'),
        ),
    ]
