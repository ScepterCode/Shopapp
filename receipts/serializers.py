from rest_framework import serializers
from .models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ['id', 'invoice', 'receipt_number', 'created_at', 'payment_method', 'amount_paid', 'note']
