from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, VendorExtraForm
from accounts.decorators import vendor_required, customer_required


# --------------------------
# Register view
# --------------------------
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            if user.user_type == 'vendor':
                return redirect('vendor_form')  # redirect to vendor extra form
            else:
                return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


# --------------------------
# Login view
# --------------------------
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


# --------------------------
# Logout view
# --------------------------
def logout_view(request):
    logout(request)
    return redirect('home')


# --------------------------
# Vendor extra form view
# --------------------------
@vendor_required
def vendor_form(request):
    if request.method == 'POST':
        form = VendorExtraForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.save()
            return redirect('vendor_dashboard')
    else:
        form = VendorExtraForm()
    
    return render(request, 'accounts/vendor_form.html', {'form': form})


# --------------------------
# Vendor dashboard (protected)
# --------------------------
@vendor_required
def vendor_dashboard(request):
    return render(request, 'accounts/vendor_dashboard.html')


# --------------------------
# Product list (customer only)
# --------------------------
@customer_required
def product_list(request):
    return render(request, 'product_list.html')
