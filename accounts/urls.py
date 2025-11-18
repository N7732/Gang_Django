from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),  # Homepage → Login page
    path('login/', CustomLoginView.as_view(), name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('register/', views.register, name='register'),
    path('vendor/', views.vendor_form, name='vendor_form'),


    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('products/', views.product_list, name='product_list'),
]
