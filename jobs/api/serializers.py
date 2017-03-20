from rest_framework import serializers
from rest_framework.serializers import (
    Serializer)

from jobs.models import Job


class JobReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'user_id', 'vehicle_id', 'job_startdate', 'job_enddate', 'job_source', 'job_destination',
                  'job_status',
                  ]
        model = Job
        read_only_fields = ('id',)


# class JobCreateUpdateSerializer(Serializer):
#     id = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     user_id = serializers.CharField(required=True, allow_blank=True, max_length=100)
#     vehicle_id = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     job_startdate = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     job_enddate = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     job_source = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     job_destination = serializers.CharField(required=False, allow_blank=True, max_length=100)
#
#     class Meta:
#         fields = [
#             'id', 'user_id', 'vehicle_id', 'job_startdate', 'job_enddate', 'job_source', 'job_destination',
#         ]

class JobCreateUpdateSerializer(Serializer):
    id = serializers.CharField(required=False, allow_blank=True, max_length=100)
    is_deleted = serializers.BooleanField(required=False)
    user_id = serializers.BooleanField(required=False)
    vehicle_id = serializers.BooleanField(required=False)
    job_startdate = serializers.BooleanField(required=False)
    job_enddate = serializers.BooleanField(required=False)
    job_source = serializers.BooleanField(required=False)
    job_destination = serializers.BooleanField(required=False)

    class Meta:
        fields = [
            'id', 'user_id', 'vehicle_id', 'job_startdate', 'job_enddate', 'job_source', 'job_destination',
            'is_deleted'
        ]
