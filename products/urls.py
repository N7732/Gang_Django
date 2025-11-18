from django.urls import path
from . import views

urlpatterns = [
    # Vendor
    path("vendor/dashboard/", views.Vendor_Dashboard, name="vendor_dashboard"),
    path("products/<int:pk>/", views.Product_List, name="product_list"),
    path("vendor/products/add/", views.Add_Product, name="add_product"),

    # Customer
    path("", views.Homepage, name="homepage"),
    path("products/", views.Product_List, name="product_list"),
    path("vendor/products/", views.Product_Detail, name="product_detail")
]
