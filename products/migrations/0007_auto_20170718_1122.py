# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170715_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricetag',
            name='product',
        ),
        migrations.DeleteModel(
            name='PriceTag',
        ),
    ]
