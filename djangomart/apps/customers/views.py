from datetime import timezone
from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from apps.customers.models import Customer  # Import your Customer model
from apps.products.models import Admin
from apps.customers.forms import CustomerSignUpForm  # Import your Admin model
from apps.orders.models import OrderProduct, Orders
from apps.products.models import Admin, Product
from apps.customers.models import Cart, CartProduct, Customer
from django.contrib.auth.decorators import login_required

# @login_required
from django.shortcuts import get_object_or_404, redirect
from apps.products.models import Product
from .models import Cart, CartProduct, Customer


# View to handle adding product to the cart
def add_to_cart(request, product_id):
    # Assuming user is authenticated
    customer = request.user  # Get the logged-in customer
    product = get_object_or_404(Product, pk=product_id)
    
    # Find or create a cart for the customer
    cart, created = Cart.objects.get_or_create(CustomerID=customer)

    # Check if the product is already in the cart
    cart_product, created = CartProduct.objects.get_or_create(
        Product_ID=product,
        CustomerID=customer,
        Cart_ID=cart,
        defaults={'Quantity': 1}
    )

    # If the product is already in the cart, update the quantity
    if not created:
        cart_product.Quantity += 1
        cart_product.save()

    # Redirect to the cart page after adding the product
    return redirect('cart')

def remove_from_cart(request, cart_product_id):
    cart_product = get_object_or_404(CartProduct, pk=cart_product.id)
    cart_product.delete()
    
    # Redirect back to the cart page after removal
    return redirect('cart')

@login_required
def cart_view(request):
    cart = get_object_or_404(Cart, CustomerID=request.user)
    cart_products = CartProduct.objects.filter(Cart_ID=cart)

    total_price = sum([item.Product_ID.Price * item.Quantity for item in cart_products])
    
    context = {
        'cart_products': cart_products,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)
from django.shortcuts import render
from .models import Cart, CartProduct

# # View to display the cart
def cart(request):
    customer = request.user  # Get the logged-in customer
    cart = Cart.objects.filter(CustomerID=customer).first()  # Get the cart for the customer

    # Get all products in the cart
    cart_products = CartProduct.objects.filter(Cart_ID=cart)

    context = {
        'cart': cart,
        'cart_products': cart_products
    }

    return render(request, 'cart.html', context)


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)

                if isinstance(user, Customer):
                    return redirect('home')  # Redirect to customer's home
                elif isinstance(user, Admin):
                    return redirect('admin_dashboard')  # Redirect to admin's dashboard

            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def signup_view(request):
    return render(request, 'signup.html')

def account_view(request):
    return render(request, 'account.html')

# def cart_view(request):
#     return render(request, 'cart.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home page after logout

def signup_view(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            return redirect('login')  # Redirect to a homepage or another page
    else:
        form = CustomerSignUpForm()
    
    return render(request, 'signup.html', {'form': form})