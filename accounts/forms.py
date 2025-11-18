from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Vendor

# ---------------------------
# User Registration Form
# ---------------------------
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'phone', 'location']

# ---------------------------
# Vendor Extra Form
# ---------------------------
class VendorExtraForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['company_name', 'business_description']
