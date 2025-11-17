from django import forms

class account(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    email = forms.EmailField(
        max_length=30,
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password_Confirm = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )
    Location = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'})
    )
    phone = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    User_Type = forms.ChoiceField(
        choices=[('Vendor', 'Vendor'), ('Customer', 'Customer')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
