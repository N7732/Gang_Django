from django import forms
from .models import Custom_user
from django.contrib.auth.forms import UserCreationForm

class account(UserCreationForm):
    class Meta:
        model = Custom_user
        fields = ['username', 'email', 'user_type', 'phone', 'location', 'password1', 'password2']  