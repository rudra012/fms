# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20170324_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_status',
            field=models.IntegerField(blank=True, default=1, max_length=255, null=True),
        ),
    ]
