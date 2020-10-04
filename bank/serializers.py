from rest_framework import serializers

from .data import TRANSACTION_ENTRY_STR, TRANSACTION_OUT_STR
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'id_number', 'creation_date']


class TransactionSerializer(serializers.Serializer):
    transaction_type = serializers.ChoiceField(
        choices=[TRANSACTION_ENTRY_STR, TRANSACTION_OUT_STR]
    )
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
