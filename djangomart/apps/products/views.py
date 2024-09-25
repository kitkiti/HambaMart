# Create your views here.
# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from apps.products.models import Product, ProductTags
from apps.products.models import Product
from apps.products.forms import ProductForm


def product_search(request):
    search_query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    selected_categories = request.GET.getlist('categories')

    # Base query for the products
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
        'search_query': search_query,  # So the search query can be shown in the template
        'min_price': min_price,
        'max_price': max_price,
        'selected_categories':  selected_categories,
    }

    return render(request, 'product_search.html', context)
def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def admin_view(request):
    return render(request, 'admin_dashboard.html')

def deleteproduct_view(request):
    return render(request, 'delete_product.html')

def editproduct_view(request):
    return render(request, 'search_edit_product.html')

def product_details_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'product': product})


def add_product_view(request):
    if request.method== 'POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the product and associated tags
            return redirect('admin_dashboard')  # Redirect to the product list or another page
    else:
        form= ProductForm()
    return render(request, 'add_product.html', {'form': form})

def search_and_edit_product(request):
    product = None  # Initialize product as None
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Get the product ID from the search form
        try:
            product = Product.objects.get(Product_ID=product_id)  # Fetch product by ID
        except Product.DoesNotExist:
            product = None  # If the product doesn't exist, set to None

        if product and 'edit_product' in request.POST:
            # If the edit form is submitted
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()  # Save changes
                return redirect('search_and_edit_product')  # Redirect back to search and edit page
        else:
            # If product exists but form is not submitted yet, pre-fill the form
            form = ProductForm(instance=product)
    else:
        form = None  # If no form submitted yet, form remains None

    return render(request, 'search_edit_product.html', {'form': form, 'product': product})