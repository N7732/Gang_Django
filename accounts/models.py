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

class Vendor(models.Model):
   StUTUS_CHOICES={
       ('pending','Pending'),
        ('aproved','Aproved'),
        ('rejected','Rejected'),
        }
   user=models.OneToOneField(Custom_user,on_delete=models.CASCADE,related_name='vendor_profile',limit_choices_to={'user_type':'vendor'})
   status=models.CharField(max_length=10,choices=StUTUS_CHOICES,default='pending')
   company_name=models.CharField(max_length=50)

   def __str__(self):
      return f"{self.company_name} - {self.status}"
  

    
