from rest_framework import serializers


class TransactionIdsSerializer(serializers.Serializer):
    transaction_ids = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )