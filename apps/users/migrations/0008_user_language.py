# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_users', '0007_rename_table_to_defaults'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('de', 'German')], default='de', max_length=4, verbose_name='Language'),
        ),
    ]
