# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-14 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PgMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.CharField(max_length=20)),
                ('lunch', models.CharField(max_length=20)),
                ('dinner', models.CharField(max_length=20)),
            ],
        ),
    ]
