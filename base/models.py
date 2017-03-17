# -*- coding: utf-8 -*-

from django.db import models


class BaseModel(models.Model):
    """
    An abstract base class model to add basic db fields
    """
    i_by = models.IntegerField(blank=True, null=True)
    u_by = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
