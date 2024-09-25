from django.shortcuts import render

# Create your views here.
# products/views.py
from django.shortcuts import render, get_object_or_404
from apps.products.models import Product


def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def admin_view(request):
    return render(request, 'admin_dashboard.html')

def addproduct_view(request):
    return render(request, 'add_product.html')

def editproduct_view(request):
    return render(request, 'edit_product.html')

def deleteproduct_view(request):
    return render(request, 'delete_product.html')

def product_details_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'product': product})