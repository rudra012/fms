# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicledocument',
            name='i_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicledocument',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicledocument',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicledocument',
            name='u_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='i_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='u_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
