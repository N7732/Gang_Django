from django import forms
from .models import Custom_user, Vendor
from django.contrib.auth.forms import UserCreationForm

class account(UserCreationForm):
    class Meta:
        model = Custom_user
        fields = ['username', 'email', 'user_type', 'phone', 'location', 'password1', 'password2']  
class VendorExtraForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['company_name', 'business_description']