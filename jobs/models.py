from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel

from base.models import BaseModel


class Job(TimeStampedModel, BaseModel):
    id = models.AutoField(primary_key=True, db_index=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    vehicle_id = models.CharField(max_length=255, blank=True, null=True)
    job_startdate = models.CharField(max_length=255, blank=True, null=True)
    job_enddate = models.CharField(max_length=255, blank=True, null=True)
    job_source = models.CharField(max_length=255, blank=True, null=True)
    job_destination = models.CharField(max_length=255, blank=True, null=True)
    job_status = models.CharField(max_length=255, blank=True, null=True)
