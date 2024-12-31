
from django.db import models
from customers.models import Customer
from products.models import Product

# Model to store quotation details
class Quotation(models.Model):
    # Choices for the status of the quotation
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('CONVERTED', 'Converted'),
        ('EXPIRED', 'Expired'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="quotations")  # Links to a customer
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the quotation was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')  # Status of the quotation
    validity_period = models.PositiveIntegerField(help_text="Validity period in days")  # Validity period for the quotation
    notes = models.TextField(blank=True, null=True)  # Additional notes about the quotation

    def __str__(self):
        return f"Quotation {self.id} for {self.customer.name}"  # String representation for debugging

# Model to store items in a quotation
class QuotationItem(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="items")  # Links to a specific quotation
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Links to a specific product
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"  # String representation for debugging

