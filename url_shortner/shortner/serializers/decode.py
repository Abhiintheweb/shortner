
from rest_framework import serializers


class DecodeSerializer(serializers.Serializer):
    key = serializers.CharField(required=True)
