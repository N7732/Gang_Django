from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root '/' to accounts home page
def home_redirect(request):
    return redirect('home')  # 'home' is from accounts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home_redirect, name='root_redirect'),
]
