# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-14 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodmanageapp', '0010_personaldetails_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='user_image',
            field=models.ImageField(default='', upload_to='pgfoodmanagement/product_image'),
        ),
    ]
