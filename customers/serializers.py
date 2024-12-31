from rest_framework import serializers
from .models import Customer, CustomerContact, CustomerNote

class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContact
        fields = '__all__'

class CustomerNoteSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = CustomerNote
        fields = ['id', 'note', 'created_by', 'created_by_name', 'created_at', 'updated_at']
        read_only_fields = ['created_by']

class CustomerSerializer(serializers.ModelSerializer):
    contacts = CustomerContactSerializer(many=True, read_only=True)
    notes = CustomerNoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']
