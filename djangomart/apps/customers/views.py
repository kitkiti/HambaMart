from datetime import timezone
from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from apps.orders.models import OrderProduct, Orders
from apps.products.models import Admin, Product
from apps.customers.models import Cart, CartProduct, Customer
from django.contrib.auth.decorators import login_required

# @login_required
from django.shortcuts import get_object_or_404, redirect
from apps.products.models import Product
from .models import Cart, CartProduct, Customer

# def add_to_cart(request, product_id):
#     current_user = request.user
#     product = Product.objects.get(id=product_id) #get the product
#     # If the user is authenticated
#     if current_user.is_authenticated:
#         is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
#         if is_cart_item_exists:
#             cart_items = CartItem.objects.filter(product=product, user=current_user)
#             print(cart_items)
#             item = CartItem.objects.get(product=product, user=current_user)
#             item.quantity += 1
#             item.save()
            
#         else:
#             try:
#                 cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
#             except Cart.DoesNotExist:
#                 cart = Cart.objects.create(
#                     cart_id = _cart_id(request)
#                 )
#             cart.save()
#             cart_item = CartItem.objects.create(
#                 product = product,
#                 quantity = 1,
#                 cart = cart,
#                 user = current_user
#             )
#             cart_item.save()
#         return redirect('cart')
#     else:
#         product = Product.objects.get(id=product_id)
#         try:
#             cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(
#                 cart_id = _cart_id(request)
#             )
#             cart.save()
        
#         try:
#             cart_item = CartItem.objects.get(product=product, cart=cart)
#             cart_item.quantity  += 1
#             cart_item.save()
#         except CartItem.DoesNotExist:
#             cart_item = CartItem.objects.create(
#                     product = product,
#                     quantity = 1,
#                     cart = cart,
#                 )
#             cart.save()
#     return redirect('cart')


# def remove_cart(request, product_id, cart_item_id):

#     product = get_object_or_404(Product, id=product_id)
#     try:
#         if request.user.is_authenticated:
#             cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#     except:
#         pass
#     return redirect('cart')


# def remove_cart_item(request, product_id, cart_item_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.user.is_authenticated:
#         cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
#     else:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
#     cart_item.delete()
#     return redirect('cart')


# def cart(request, total=0, quantity=0, cart_items=None):
#     try:
#         tax = 0
#         grand_total = 0
#         if request.user.is_authenticated:
#             cart_items = CartItem.objects.filter(user=request.user, is_active=True)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_items = CartItem.objects.filter(cart=cart, is_active=True)
#         for cart_item in cart_items:
#             total += (cart_item.product.price * cart_item.quantity)
#             quantity += cart_item.quantity
#         tax = (2 * total)/100
#         grand_total = total + tax
#     except ObjectDoesNotExist:
#         pass #just ignore

#     context = {
#         'total': total,
#         'quantity': quantity,
#         'cart_items': cart_items,
#         'tax'       : tax,
#         'grand_total': grand_total,
#     }
#     return render(request, 'cart/cart.html', context)

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