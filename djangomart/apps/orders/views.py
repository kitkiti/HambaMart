from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from apps.orders.models import Payment, Orders, OrderProduct
from apps.customers.models import Cart, CartProduct
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Orders, OrderProduct, Payment
from apps.customers.models import Cart, CartProduct 

@login_required
def checkout(request):
    customer = request.user
    cart = Cart.objects.filter(CustomerID=customer).first()
    cart_products = CartProduct.objects.filter(Cart_ID=cart)

    if request.method == 'POST':
        new_order = Orders.objects.create(
            Total_Price=cart.total_price,
            Status='Pending',
            Address=customer.Address, 
            created_at=timezone.now()
        )

        for cart_product in cart_products:
            OrderProduct.objects.create(
                Product_ID=cart_product.Product_ID,
                Order_ID=new_order,
                product_quantity=cart_product.Quantity
            )
        
        cart_products.delete()
        return redirect('process_payment', order_id=new_order.Order_ID) 

    context = {
        'cart_products': cart_products,
        'total_price': cart.total_price,
        'customer': customer,  
    }

    return render(request, 'checkout.html', context)


@login_required
def process_payment(request, order_id):
    order = get_object_or_404(Orders, Order_ID=order_id)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method') 
        payment = Payment.objects.create(
            CustomerID=request.user,
            Order_ID=order,
            Amount=order.Total_Price,
            Method=payment_method
        )
        
        order.Status = 'Paid'
        order.save()

        return redirect('payment_success')  

    return render(request, 'payment.html', {'order': order})


def order_confirmation(request, order_id):
    order = Orders.objects.get(pk=order_id)
    order_products = OrderProduct.objects.filter(Order_ID=order)
    context = {
        'order': order,
        'order_products': order_products
    }
    return render(request, 'order_confirmation.html', context)

def payment_success(request):
    return render(request, 'payment_success.html')

