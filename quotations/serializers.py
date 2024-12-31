from rest_framework import serializers
from .models import Quotation, QuotationItem

# Serializer for quotation items
class QuotationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationItem
        fields = ['id', 'product', 'quantity', 'price']  # Fields to include in the API

# Serializer for quotations
class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemSerializer(many=True, read_only=True)  # Nested serializer for items

    class Meta:
        model = Quotation
        fields = ['id', 'customer', 'status', 'validity_period', 'notes', 'created_at', 'updated_at', 'items']  # Fields to include in the API
