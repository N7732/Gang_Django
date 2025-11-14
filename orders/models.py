from django.db import models
from accounts.models import Custom_user
from products.models import Product

# Create your models here.
class Order(models.Model):
    Customer_details=models.ForeignKey(Custom_user)
    total=models.IntegerField(max_length=10)
    status={
        ("Paid","paid"),
        ("Pending","pending")
    }
    status=models.CharField(max_length=20,choices=status)
    delivery_address=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=15)
    created_at=models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.Customer_details} and {self.status} and also{self.total}"
class OrderItem(models.Model):
    Order=models.ForeignKey(Order)
    product=models.ForeignKey(Product)
    quantity=models.IntegerField(max_length=20)
    price=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.Order},{self.quantity}"
    

