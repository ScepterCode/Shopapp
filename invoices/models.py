
from django.db import models
from customers.models import Customer
from products.models import Product

# Model for managing invoices
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="invoices")  # Link to a customer
    invoice_number = models.CharField(max_length=20, unique=True)  # Unique invoice number
    created_at = models.DateTimeField(auto_now_add=True)  # Invoice creation date
    due_date = models.DateField()  # Payment due date
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total invoice amount
    status = models.CharField(max_length=20, choices=[('PAID', 'Paid'), ('PENDING', 'Pending'), ('OVERDUE', 'Overdue')], default='PENDING')  # Payment status

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer.name}"

# Model for items on an invoice
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")  # Link to a specific invoice
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Product associated with the invoice item
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

