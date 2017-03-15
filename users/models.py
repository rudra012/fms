from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager
# Create your models here.
from django_extensions.db.models import TimeStampedModel

from base.models import BaseModel
from fms import settings


class User(AbstractUser,BaseModel,TimeStampedModel):
    # profile_name = models.CharField(_('profile_name'), max_length=30, blank=True)
    date_of_birth=models.DateTimeField(blank=True, null=True)
    group_id=models.CharField(max_length=30,blank=True, null=True)
    mobile_no = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=30,blank=True, null=True)
    city_name = models.CharField(max_length=30,blank=True, null=True)
    state_name = models.CharField(max_length=30,blank=True, null=True)
    postal_code = models.CharField(max_length=30,blank=True, null=True)
    country_id = models.CharField(max_length=30, blank=True, null=True)
    employee_no = models.CharField(max_length=30, blank=True, null=True)
    job_title = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateTimeField(max_length=30, blank=True, null=True)
    leave_date = models.DateTimeField(max_length=30, blank=True, null=True)
    user_type = models.CharField(max_length=30, blank=True, null=True)
    license_no = models.CharField(max_length=30, blank=True, null=True)
    license_region = models.CharField(max_length=30, blank=True, null=True)
    company_id = models.CharField(max_length=30, blank=True, null=True)

    #image = models.ImageField(upload_to=settings.MEDIA_USER_IMAGE, blank=True, null=True, default="")