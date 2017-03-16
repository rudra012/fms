from rest_framework import serializers

from rest_framework.serializers import (
    Serializer)


class GroupCreateUpdateSerializer(Serializer):
    group_name = serializers.CharField(required=True)
    is_deleted= serializers.CharField(required=False)
    id = serializers.CharField(required=False)

    class Meta:
        fields = [
            'group_name ',

        ]