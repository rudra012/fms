from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
from django_extensions.db.models import TimeStampedModel


class Vehicle(TimeStampedModel):
    id = models.AutoField(primary_key=True, db_index=True)
    vehicle_name = models.CharField(max_length=255, blank=True, null=True)
    vin_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_make = models.CharField(max_length=255, blank=True, null=True)
    vehicle_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_year = models.CharField(max_length=255, blank=True, null=True)
    vehicle_license = models.CharField(max_length=255, blank=True, null=True)
    registration_state = models.CharField(max_length=255, blank=True, null=True)
    vehiclestatus_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.CharField(max_length=1, blank=True, null=True, default='n')
    ownership = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    i_by = models.IntegerField(blank=True, null=True)
    u_by = models.IntegerField(blank=True, null=True)


class VehicleDocument(TimeStampedModel):
    id = models.AutoField(primary_key=True, db_index=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    doc_name = models.CharField(max_length=255, blank=True, null=True)
    doc_date = models.CharField(max_length=255, blank=True, null=True)
    doc_type = models.CharField(max_length=255, blank=True, null=True)
    doc_location = models.CharField(max_length=255, blank=True, null=True)
    is_primary = models.CharField(max_length=255, blank=True, null=True)


class VehicleStatus(TimeStampedModel):
    id = models.AutoField(primary_key=True, db_index=True)
    vehicle_id = models.IntegerField(blank=True, null=True)
    vehiclestatus_name = models.CharField(max_length=255, blank=True, null=True)
