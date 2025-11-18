from django.db import models
from django.conf import settings  # <-- always use this for custom user
from products.models import Product

class Order(models.Model):
    customer_details = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # <-- corrected
        on_delete=models.CASCADE
    )
    total = models.IntegerField(null=True, blank=True)
    
    STATUS_CHOICES = [
        ("Paid", "Paid"),
        ("Pending", "Pending"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    delivery_address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)  # safer than IntegerField
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_details} - {self.status} - {self.total}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order} - {self.product} x {self.quantity}"
