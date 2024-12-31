
from django.contrib import admin
from .models import Customer, CustomerContact, CustomerNote

class CustomerContactInline(admin.TabularInline):
    model = CustomerContact
    extra = 1

class CustomerNoteInline(admin.TabularInline):
    model = CustomerNote
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer_type', 'email', 'phone', 'is_active', 'created_at')
    list_filter = ('customer_type', 'is_active', 'created_at')
    search_fields = ('name', 'email', 'phone')
    inlines = [CustomerContactInline, CustomerNoteInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CustomerContact)
class CustomerContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'contact_type', 'email', 'phone', 'is_primary')
    list_filter = ('contact_type', 'is_primary')
    search_fields = ('name', 'email', 'phone', 'customer__name')

@admin.register(CustomerNote)
class CustomerNoteAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_by', 'created_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('customer__name', 'note')
    readonly_fields = ('created_at', 'updated_at')
