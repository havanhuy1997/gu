# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-27 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0018_auto_20161028_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='date_approved',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commission',
            name='date_processed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commission',
            name='date_rejected',
            field=models.DateField(blank=True, null=True),
        ),
    ]
