from datetime import timezone
from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from apps.customers.models import Customer  
from apps.products.models import Admin
from apps.customers.forms import CustomerSignUpForm  
from apps.orders.models import OrderProduct, Orders
from apps.products.models import Admin, Product
from apps.customers.models import Cart, CartProduct, Customer
from django.contrib.auth.decorators import login_required
from apps.customers.forms import CustomerProfileForm

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    if request.user.is_staff:
        return redirect('home')

    customer = request.user  
    product = get_object_or_404(Product, pk=product_id)
    if product.Stock <= 0:
        messages.error(request, 'This product is out of stock.')
        return redirect('product_detail', product_id=product_id)
    
    cart, created = Cart.objects.get_or_create(CustomerID=customer)

    try:
        cart_product = CartProduct.objects.get(Product_ID=product, CustomerID=customer, Cart_ID=cart)
        cart_product.Quantity += 1
        cart_product.save()
    
    except CartProduct.DoesNotExist:
        CartProduct.objects.create(
            Product_ID=product,
            CustomerID=customer,
            Cart_ID=cart,
            Quantity=1
        )

    return redirect('cart')

def remove_from_cart(request, cart_id, product_id):
    cart_product = CartProduct.objects.filter(Cart_ID=cart_id, Product_ID=product_id)
    cart_product.delete()
    return redirect('cart')

def cart_view(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    if request.user.is_staff:
        return redirect('home')
    cart = get_object_or_404(Cart, CustomerID=request.user)
    cart_products = CartProduct.objects.filter(Cart_ID=cart)

    total_price = sum([item.Product_ID.Price * item.Quantity for item in cart_products])
    cart.total_price = total_price
    cart.save()
    context = {
        'cart_products': cart_products,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)




def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)

                if isinstance(user, Customer):
                    next_url = request.GET.get('next', 'home')   # Redirect to customer's home
                elif isinstance(user, Admin):
                    next_url = request.GET.get('next', 'admin_dashboard')  # Redirect to admin's dashboard
                else:
                    next_url = 'home'  # Default to home for any other cases

                return redirect(next_url)
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def account_view(request):
    if not request.user.is_authenticated:
        return redirect(f'/login/?next={request.path}')
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return render(request, 'account.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home page after logout

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            messages.success(request, "You have successfully created an account.")
            return redirect('login')  # Redirect to a homepage or another page
    else:
        form = CustomerSignUpForm()
    
    return render(request, 'signup.html', {'form': form})



@login_required
def profile_view(request):
    customer = Customer.objects.get(Email=request.user.Email)  # Adjust based on how you manage user sessions

    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('account')  # Redirect to the profile page after saving
    else:
        form = CustomerProfileForm(instance=customer)

    return render(request, 'account.html', {'form': form})