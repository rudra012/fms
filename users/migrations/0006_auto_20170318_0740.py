# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170316_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_person',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact_person_email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact_person_phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='website_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, default='u', max_length=30, null=True),
        ),
    ]
