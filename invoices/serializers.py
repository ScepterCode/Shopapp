from rest_framework import serializers
from .models import Invoice, InvoiceItem

# Serializer for invoice items
class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['id', 'product', 'quantity', 'price']

# Serializer for invoices
class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'customer', 'invoice_number', 'created_at', 'due_date', 'total_amount', 'status', 'items']
