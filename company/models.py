from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

from base.models import BaseModel


class Company(TimeStampedModel,BaseModel):
    id = models.AutoField(primary_key=True, db_index=True)
    company_name=models.CharField(max_length=255, blank=True, null=True)
