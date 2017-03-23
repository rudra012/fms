from rest_framework import serializers
from rest_framework.serializers import (
    Serializer)

from jobs.models import Job


class JobReadSerializer(serializers.ModelSerializer):
    user_first_name = serializers.SerializerMethodField('is_first_name')
    vehicle_name = serializers.SerializerMethodField('is_vehicle_name')

    def is_first_name(self, job):
        return job.user_first_name

    def is_vehicle_name(self,job):
        return job.vehicle_name

    class Meta:
        fields = ['id', 'user_id', 'vehicle_id', 'job_startdate', 'job_enddate', 'job_source', 'job_destination',
                  'job_status','user_first_name','vehicle_name'
                  ]
        model = Job
        read_only_fields = ('id',)


class JobCreateUpdateSerializer(Serializer):
    id = serializers.CharField(required=False, allow_blank=True, max_length=100)
    is_deleted = serializers.CharField(required=False)
    user_id  = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # vehicle_id = serializers.CharField(required=False, allow_blank=True, max_length=100)
    job_startdate = serializers.CharField(required=False, allow_blank=True, max_length=100)
    job_enddate = serializers.CharField(required=False, allow_blank=True, max_length=100)
    job_source = serializers.CharField(required=False, allow_blank=True, max_length=100)
    job_destination = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        fields = [
            'id', 'user_id', 'vehicle_id', 'job_startdate', 'job_enddate', 'job_source', 'job_destination',
            'is_deleted'
        ]


