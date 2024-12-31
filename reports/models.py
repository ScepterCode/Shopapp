

from django.db import models
from django.conf import settings  # Import settings for AUTH_USER_MODEL

# Model for storing generated reports
class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('SALES', 'Sales Report'),
        ('PRODUCT', 'Product Analysis'),
        ('CUSTOMER', 'Customer History'),
        ('PAYMENT', 'Payment Report'),
        ('TAX', 'Tax Report'),
    ]

    report_name = models.CharField(max_length=255)  # Name of the report
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)  # Type of report
    generated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="generated_reports")  # Use AUTH_USER_MODEL
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for report creation
    file_path = models.FileField(upload_to='reports/')  # Path to the stored file (PDF/Excel)

    def __str__(self):
        return f"{self.report_name} ({self.report_type})"

# Model for managing uploaded documents
class Document(models.Model):
    title = models.CharField(max_length=255)  # Document title
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="uploaded_documents")  # Use AUTH_USER_MODEL
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for document upload
    file_path = models.FileField(upload_to='documents/')  # Path to the uploaded document
    description = models.TextField(blank=True, null=True)  # Optional description of the document

    def __str__(self):
        return self.title
