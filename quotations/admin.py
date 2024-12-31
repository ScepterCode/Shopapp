
from django.contrib import admin
from .models import Quotation, QuotationItem

# Inline for managing quotation items directly in the admin panel
class QuotationItemInline(admin.TabularInline):
    model = QuotationItem
    extra = 1  # Number of empty forms displayed for new items

# Admin class for managing quotations
@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at', 'updated_at')  # Fields displayed in the admin list view
    list_filter = ('status', 'created_at')  # Filters for the admin list view
    search_fields = ('customer__name',)  # Searchable fields
    inlines = [QuotationItemInline]  # Inline management for quotation items

