from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

from base.models import BaseModel


class Fuel(TimeStampedModel, BaseModel):
    vehicle_id = models.CharField(max_length=255, blank=True, null=True)
    fuel_date = models.CharField(max_length=255, blank=True, null=True)
    odometer_id = models.CharField(max_length=255, blank=True, null=True)
    fuel_measure = models.CharField(max_length=255, blank=True, null=True)
    fuel_price = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    fuel_type = models.CharField(max_length=255, blank=True, null=True)
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
