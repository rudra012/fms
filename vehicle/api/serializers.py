from rest_framework import serializers

from rest_framework.serializers import (
    Serializer)


class VehiclCreateUpdateSerializer(Serializer):
    vehicle_name = serializers.CharField(required=True)

    class Meta:
        fields = [
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
        ]


class UpdateVehicleSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    vehicle_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        fields = [
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
        ]