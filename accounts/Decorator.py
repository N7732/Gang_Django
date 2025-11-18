from django.shortcuts import render, redirect
from django.contrib import messages

def vendor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:# Check if user is authenticated
            messages.error(request, "You must be logged in to access this page.")
            return redirect('login')
        
        if not hasattr(request.user, 'user_type'):# Check if user_type attribute exists
            messages.error(request, "User type is not defined.")
            return redirect('home')
        
        if request.user.user_type != 'vendor':# Check if user is a vendor
            messages.error(request, "You do not have permission to access this page.")
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view