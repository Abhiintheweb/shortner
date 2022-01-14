from rest_framework import serializers


class EncodeSerializer(serializers.Serializer):
    url = serializers.CharField(required=True)
