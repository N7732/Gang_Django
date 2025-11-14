from django.db import models

# Create your models here.
class Custom_user(models.Model):
    user_type={
        ("Vendor","vendor"),
        ('Customer',"customer"),
    }
    user_type=models.CharField(max_length=10, choices=user_type)
    phone=models.IntegerField(max_length=15)
    location=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.user_type} and {self.location}"
    
