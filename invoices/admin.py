from django.contrib import admin

from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer', 'total_amount', 'status', 'created_at', 'due_date')
    list_filter = ('status', 'created_at', 'due_date')
    search_fields = ('invoice_number', 'customer__name')
    inlines = [InvoiceItemInline]

