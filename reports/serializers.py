from rest_framework import serializers
from .models import Report, Document

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'report_name', 'report_type', 'generated_by', 'created_at', 'file_path']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'uploaded_by', 'uploaded_at', 'file_path', 'description']
