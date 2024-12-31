
from django.contrib import admin
from .models import Receipt

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'invoice', 'amount_paid', 'payment_method', 'created_at')
    list_filter = ('payment_method', 'created_at')
    search_fields = ('receipt_number', 'invoice__invoice_number')

