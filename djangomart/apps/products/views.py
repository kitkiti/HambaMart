from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from apps.customers.models import Cart, CartProduct
from apps.products.forms import ProductForm
from apps.products.models import Product, ProductTags
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.customers.models import Customer

def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    if not request.user.is_staff:
        return redirect('home')
    else:
        total_products = Product.objects.count() 
        total_customers = Customer.objects.count() 
        context = {
            'total_products': total_products,
            'total_customers': total_customers,
        }
    
        return render(request, 'admin_dashboard.html', context)

def product_search(request):
    search_query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    selected_categories = request.GET.getlist('categories')

   
    products = Product.objects.all()

    if search_query:
        products = products.filter(
            Q(Title__icontains=search_query) |
            Q(Description__icontains=search_query) |
            Q(producttags__Tag__icontains=search_query)
        ).distinct()

    if min_price:
        products = products.filter(Price__gte=min_price)
    if max_price:
        products = products.filter(Price__lte=max_price)

    if selected_categories:
        products = products.filter(producttags__Tag__in=selected_categories).distinct()
    context = {
        'products': products,
        'search_query': search_query,  
        'min_price': min_price,
        'max_price': max_price,
        'selected_categories':  selected_categories,
    }

    return render(request, 'product_search.html', context)

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def base(request):
    return render(request, 'base.html')

def deleteproduct_view(request):
    return render(request, 'delete_product.html')

def editproduct_view(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'search_edit_product.html')

def product_details_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'product': product})


def add_product_view(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    if not request.user.is_staff:
        return redirect('home')
    if request.method== 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('admin_dashboard')  
    else:
        form= ProductForm()
    return render(request, 'add_product.html', {'form': form})

def search_and_edit_product(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    if not request.user.is_staff:
        return redirect('home')
    product = None  
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  
        try:
            product = Product.objects.get(Product_ID=product_id)  
        except Product.DoesNotExist:
            product = None 

        if product and 'edit_product' in request.POST:
            
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save() 
                return redirect('search_and_edit_product')  
        else:
            
            form = ProductForm(instance=product)
    else:
        form = None  

    return render(request, 'search_edit_product.html', {'form': form, 'product': product})


def product_delete_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, Product_ID=product_id)

        if 'delete' in request.POST: 
            product.delete()
            messages.success(request, 'Product deleted successfully!')
            return redirect('deleteproduct_view') 

    else:
        product_id = request.GET.get('product_id') 
        product = None
        if product_id:
            product = Product.objects.filter(Product_ID=product_id).first()

    return render(request, 'delete_product.html', {'product': product})