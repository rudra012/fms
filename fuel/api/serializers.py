from rest_framework import serializers

from fuel.models import Fuel
from rest_framework.serializers import (
    Serializer)


class FuelReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['vehicle_id', 'fuel_date', 'odometer_id', 'fuel_measure', 'fuel_price', 'currency', 'fuel_type',
                  'vendor_name', 'comment']
        model = Fuel
        read_only_fields = ('vehicle_id',)


class FuelCreateUpdateSerializer(Serializer):
    vehicle_id = serializers.CharField(required=False, allow_blank=True, max_length=100)
    fuel_date = serializers.CharField(required=False, allow_blank=True, max_length=100)
    odometer_id = serializers.CharField(required=False, allow_blank=True, max_length=100)
    fuel_measure = serializers.CharField(required=False, allow_blank=True, max_length=100)
    fuel_price = serializers.CharField(required=False, allow_blank=True, max_length=100)
    currency = serializers.CharField(required=False, allow_blank=True, max_length=100)
    fuel_type = serializers.CharField(required=False, allow_blank=True, max_length=100)
    vendor_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    comment = serializers.CharField(required=False, allow_blank=True, max_length=100)
    is_deleted = serializers.CharField(required=False, allow_blank=True, max_length=100)
    id = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        fields = [
            'vehicle_id', 'fuel_date', 'odometer_id', 'fuel_measure', 'fuel_price', 'currency', 'fuel_type',
            'vendor_name', 'comment'
        ]
