from rest_framework import serializers

from rest_framework.serializers import (
    Serializer)


class CompanyCreateUpdateSerializer(Serializer):
    company_name = serializers.CharField(required=True)
    id = serializers.CharField(required=False)

    class Meta:
        fields = [
            'id',
            'company_name ',
        ]
