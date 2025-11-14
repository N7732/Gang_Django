from django.contrib.auth.models import AbstractUser
from django.db import models

class Custom_user(AbstractUser):
    USER_TYPES = [
        ("vendor", "Vendor"),
        ("customer", "Customer"),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['user_type', 'phone', 'location']
