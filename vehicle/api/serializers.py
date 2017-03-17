from rest_framework import serializers

from rest_framework.serializers import (
    Serializer)


class VehiclCreateUpdateSerializer(Serializer):
    id=serializers.CharField(required=False,allow_blank=True, max_length=100)
    vehicle_name = serializers.CharField(required=True,allow_blank=True, max_length=100)
    vin_no = serializers.CharField(required=False)
    vehicle_make = serializers.CharField(required=False,allow_blank=True, max_length=100)
    vehicle_model = serializers.CharField(required=False,allow_blank=True, max_length=100)
    vehicle_year = serializers.CharField(required=False,allow_blank=True, max_length=100)
    vehicle_license = serializers.CharField(required=False,allow_blank=True, max_length=100)
    registration_state = serializers.CharField(required=False,allow_blank=True, max_length=100)
    vehiclestatus_id = serializers.CharField(required=False,allow_blank=True, max_length=100)
    group_id = serializers.CharField(required=False,allow_blank=True, max_length=100)
    contact_id = serializers.CharField(required=False,allow_blank=True, max_length=100)
    ownership = serializers.CharField(required=False,allow_blank=True, max_length=100)
    is_deleted = serializers.BooleanField(required=False)

    class Meta:
        fields = [
            'id',
            'vehicle_name ',
            'vin_no ',
            'vehicle_make ',
            'vehicle_model ',
            'vehicle_year ',
            'vehicle_license ',
            'registration_state ',
            'vehiclestatus_id ',
            'group_id ',
            'contact_id ',
            'ownership ',
            'company_id ',
            'is_deleted',
        ]
