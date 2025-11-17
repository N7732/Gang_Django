from django.db import models
from accounts.models import Custom_user
from products.models import Product

# Create your models here.
class Order(models.Model):
    Customer_details=models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    total=models.IntegerField(null=True,blank=True)
    status={
        ("Paid","paid"),
        ("Pending","pending")
    }
    status=models.CharField(max_length=20,choices=status)
    delivery_address=models.CharField(max_length=50)
    phone=models.IntegerField(null=True,blank=True)
    created_at=models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.Customer_details} and {self.status} and also{self.total}"
class OrderItem(models.Model):
    Order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.Order},{self.quantity}"
    

