# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_auto_20170728_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='detilpenjualan',
            name='harga_jual',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='detilpenjualan',
            name='laba',
            field=models.IntegerField(default=0),
        ),
    ]