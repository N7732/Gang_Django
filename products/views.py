from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.decorators import vendor_required
from orders.models import OrderItem
from .models import Product
from .form import ProductForm  

@vendor_required
def Vendor_Dashboard(request):
    vendor = request.user.vendor
    products = Product.objects.filter(vendor=vendor)

    context = {
        'total_products': products.count(),
        'active_products': products.filter(status='active').count(),
        'out_of_stock': products.filter(stock=0).count(),
        'pending_orders': OrderItem.objects.filter(
            product__vendor=vendor,
            order__status='pending'
        ).count(),
        'recent_products': products.order_by('-created_at')[:5],
    }
    return render(request, 'vendor/dashboard.html', context)

@vendor_required
def Add_Product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.status = "active"
            product.save()
            messages.success(request, "Product added successfully!")
            return redirect('vendor_products')
    else:
        form = ProductForm()
    return render(request, 'vendor/add_product.html', {'form': form})

from django.shortcuts import get_object_or_404

def Product_Detail(request, pk):
    product = get_object_or_404(Product, pk=pk, status='active')
    return render(request, "customer/product_detail.html", {"product": product})

@vendor_required
def Vendor_Products(request):
    vendor = request.user.vendor
    products = Product.objects.filter(vendor=vendor).order_by('-created_at')

    return render(request, "vendor/product_list.html", {
        "products": products,
    })
from django.core.paginator import Paginator

def Product_List(request):
    products = Product.objects.filter(status='active')

    sort = request.GET.get("sort")
    if sort == "price_low":
        products = products.order_by("price")
    elif sort == "price_high":
        products = products.order_by("-price")
    else:
        products = products.order_by("-created_at")

    p = Paginator(products, 12)
    page = request.GET.get("page")
    products = p.get_page(page)

    return render(request, "customer/product_list.html", {"products": products})

def Homepage(request):
    newest = Product.objects.filter(status='active').order_by('-created_at')[:8]
    return render(request, "customer/home.html", {"products": newest})



# from django.core.paginator import Paginator
# def product_list(request):
#     products = Product.objects.filter(status='active').order_by('-created_at')
#     paginator = Paginator(products, 10)  # Show 10 products per page

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, "customer/product_list.html", {"page_obj": page_obj})
