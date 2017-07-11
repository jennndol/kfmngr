# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_product_weight'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Supplier')),
            ],
        ),
    ]