# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_job_nbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_nbr',
            field=models.CharField(blank=True, default=1, max_length=255, null=True),
        ),
    ]
