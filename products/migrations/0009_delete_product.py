# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_produk'),
        ('transactions', '0007_auto_20170726_1425'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
