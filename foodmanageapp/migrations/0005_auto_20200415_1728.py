# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-15 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmanageapp', '0004_mealagreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealagreement',
            name='breakfast',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mealagreement',
            name='dinner',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mealagreement',
            name='lunch',
            field=models.CharField(max_length=10),
        ),
    ]