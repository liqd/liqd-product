# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 15:17
from __future__ import unicode_literals

from django.db import migrations

sql = """UPDATE django_content_type
         SET app_label = 'a4_candy_organisations'
         WHERE app_label = 'liqd_product_organisations';"""

reverse_sql = """UPDATE django_content_type
                 SET app_label = 'liqd_product_organisations';
                 WHERE app_label = 'a4_candy_organisations';"""


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_organisations', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(sql, reverse_sql)
    ]
