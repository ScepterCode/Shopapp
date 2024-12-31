
from django.db import models
from accounts.models import CustomUser

class Customer(models.Model):
    CUSTOMER_TYPES = (
        ('regular', 'Regular'),
        ('corporate', 'Corporate'),
        ('wholesale', 'Wholesale')
    )
    
    name = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    tax_number = models.CharField(max_length=50, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.name} ({self.get_customer_type_display()})"

class CustomerContact(models.Model):
    CONTACT_TYPES = (
        ('primary', 'Primary'),
        ('billing', 'Billing'),
        ('shipping', 'Shipping'),
        ('technical', 'Technical')
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=50, blank=True)
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.customer.name} ({self.get_contact_type_display()})"

class CustomerNote(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notes')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Note for {self.customer.name} - {self.created_at.date()}"


