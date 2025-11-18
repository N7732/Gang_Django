from django.contrib.auth.models import AbstractUser
from django.db import models

# ---------------------------
# Custom User Model
# ---------------------------
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("vendor", "Vendor"),
        ("customer", "Customer"),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')
    phone = models.CharField(max_length=20, blank=True, null=True)  # safer than IntegerField
    location = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.user_type}) - {self.location}"


# ---------------------------
# Vendor Profile Model
# ---------------------------
class Vendor(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='vendor_profile',
        limit_choices_to={'user_type': 'vendor'}
    )
    company_name = models.CharField(max_length=50)
    business_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.company_name} - {self.status}"
