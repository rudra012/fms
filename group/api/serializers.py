from rest_framework import serializers

from rest_framework.serializers import (
    Serializer)

from group.models import Group


class GroupCreateUpdateSerializer(Serializer):
    group_name = serializers.CharField(required=True)
    is_deleted= serializers.CharField(required=False)
    id = serializers.CharField(required=False)

    class Meta:
        fields = [
            'group_name ',
        ]


class GroupReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['group_name','id']
        model = Group
        read_only_fields = ('id',)
        write_only_fields = ('password',)
