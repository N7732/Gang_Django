from django.shortcuts import redirect
from functools import wraps
# Vendor Only
def vendor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'vendor':
            return view_func(request, *args, **kwargs)
        return redirect('login')  # <-- change here
    return _wrapped_view

# Customer Only
def customer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'customer':
            return view_func(request, *args, **kwargs)
        return redirect('login')  # <-- change here
    return _wrapped_view
