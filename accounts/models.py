from django.contrib.auth.models import AbstractUser as Abs
from django.db import models
# Create your models here.
class Custom_user(Abs):
    user_type={
        ("Vendor","vendor"),
        ('Customer',"customer"),
    }
    user_type=models.CharField(max_length=10, choices=user_type,default='customer')
    phone=models.IntegerField(null=True,blank=True)
    location=models.CharField(max_length=50)

    def __str__(self):
      return f"{self.username} and {self.email}"
    
    def __str__(self):
        return f"{self.user_type} and {self.location}"
    
    
