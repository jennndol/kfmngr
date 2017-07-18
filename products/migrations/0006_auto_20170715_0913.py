# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_pricetag'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricetag',
            name='sku',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='pricetag',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]