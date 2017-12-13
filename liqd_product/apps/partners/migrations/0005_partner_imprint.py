# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 17:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liqd_product_partners', '0004_fix_upload_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='imprint',
            field=ckeditor.fields.RichTextField(verbose_name='Imprint', default=''),
            preserve_default=False,
        ),
    ]