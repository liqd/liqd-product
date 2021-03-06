# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 15:14
from __future__ import unicode_literals

from django.db import migrations

sql = """UPDATE django_content_type
         SET app_label = 'liqd_product_projects'
         WHERE app_label = 'meinberlin_projects';"""

reverse_sql = """UPDATE django_content_type
                 SET app_label = 'meinberlin_projects';
                 WHERE app_label = 'liqd_product_projects';"""


class Migration(migrations.Migration):

    replaces = [('liqd_product_projects', '0002_update_content_types')]

    dependencies = [
        ('a4_candy_projects', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(sql, reverse_sql)
    ]
