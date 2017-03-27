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
    vehicle_id = serializers.CharField(required=True)
    fuel_date = serializers.CharField(required=True)
    odometer_id = serializers.CharField(required=True)
    fuel_measure = serializers.CharField(required=True)
    fuel_price = serializers.CharField(required=True)
    currency = serializers.CharField(required=True)
    fuel_type = serializers.CharField(required=True)
    vendor_name = serializers.CharField(required=True)
    comment = serializers.CharField(required=True)
    is_deleted = serializers.CharField(required=False)
    id = serializers.CharField(required=False)

    class Meta:
        fields = [
            'group_name ',
        ]
