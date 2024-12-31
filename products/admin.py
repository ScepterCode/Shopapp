
from django.contrib import admin
from .models import Category, Supplier, Product, SerialNumber, PriceHistory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at')
    search_fields = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'email', 'phone', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'contact_person', 'email')

class SerialNumberInline(admin.TabularInline):
    model = SerialNumber
    extra = 1

class PriceHistoryInline(admin.TabularInline):
    model = PriceHistory
    extra = 0
    readonly_fields = ('changed_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'stock_quantity', 'is_active')
    list_filter = ('category', 'supplier', 'is_active')
    search_fields = ('name', 'sku', 'description')
    inlines = [SerialNumberInline, PriceHistoryInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SerialNumber)
class SerialNumberAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'product', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('serial_number', 'product__name')
