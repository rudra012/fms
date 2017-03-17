from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

from base.models import BaseModel


class Group(TimeStampedModel,BaseModel):
    id = models.AutoField(primary_key=True, db_index=True)
    group_name=models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)