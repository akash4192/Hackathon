# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160929_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='orderDate',
        ),
        migrations.AddField(
            model_name='order',
            name='deliveryDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='DeliveryDate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ShipDate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
