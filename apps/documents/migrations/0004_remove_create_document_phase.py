# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from adhocracy4.phases.models import Phase


def _remove_create_phase(apps, schema_editor):
    Phase.objects.filter(
        type='a4_candy_documents:030:create_document'
    ).delete()


class Migration(migrations.Migration):

    replaces = [('meinberlin_documents', '0004_remove_create_document_phase')]

    dependencies = [
        ('a4_candy_documents', '0003_add_chapter_weight'),
    ]

    operations = [
        migrations.RunPython(_remove_create_phase)
    ]
