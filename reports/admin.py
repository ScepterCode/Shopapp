
from django.contrib import admin
from .models import Report, Document

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_name', 'report_type', 'generated_by', 'created_at')
    list_filter = ('report_type', 'created_at')
    search_fields = ('report_name',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'uploaded_at')
    search_fields = ('title',)

