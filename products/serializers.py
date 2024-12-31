from rest_framework import serializers
from .models import Category, Supplier, Product, SerialNumber, PriceHistory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SerialNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialNumber
        fields = '__all__'

class PriceHistorySerializer(serializers.ModelSerializer):
    changed_by_name = serializers.CharField(source='changed_by.username', read_only=True)

    class Meta:
        model = PriceHistory
        fields = '__all__'
        read_only_fields = ['changed_by']

class ProductSerializer(serializers.ModelSerializer):
    serial_numbers = SerialNumberSerializer(many=True, read_only=True)
    price_history = PriceHistorySerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']
