# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-16 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodmanageapp', '0007_pgmenu_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pgmenu',
            name='date',
        ),
    ]
