# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('meinberlin_ideas', '0002_idea_category')]

    dependencies = [
        ('a4categories', '__first__'),
        ('a4_candy_ideas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='a4categories.Category'),
        ),
    ]
