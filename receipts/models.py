

from django.db import models
from invoices.models import Invoice

# Model for managing receipts
class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="receipts")  # Link to an invoice
    receipt_number = models.CharField(max_length=20, unique=True)  # Unique receipt number
    created_at = models.DateTimeField(auto_now_add=True)  # Receipt creation date
    payment_method = models.CharField(
        max_length=20,
        choices=[('CASH', 'Cash'), ('CARD', 'Card'), ('BANK_TRANSFER', 'Bank Transfer')],
        default='CASH'
    )  # Payment method
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid
    note = models.TextField(blank=True, null=True)  # Optional notes

    def __str__(self):
        return f"Receipt {self.receipt_number} for Invoice {self.invoice.invoice_number}"

