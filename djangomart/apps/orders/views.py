from datetime import timezone
from django.shortcuts import get_object_or_404, render, redirect
from apps.orders.models import Payment, Orders, OrderProduct
from apps.customers.models import Cart, CartProduct
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    customer = request.user
    cart = Cart.objects.filter(CustomerID=customer).first()
    cart_products = CartProduct.objects.filter(Cart_ID=cart)

    if request.method == 'POST':
        # Create a new order
        new_order = Orders.objects.create(
            Total_Price=cart.total_price,
            Status='Pending',
            Address=customer.Address,  # You can ask the user to confirm the address
            created_at=timezone.now()
        )

        # Add all cart products to the order
        for cart_product in cart_products:
            OrderProduct.objects.create(
                Product_ID=cart_product.Product_ID,
                Order_ID=new_order,
                product_quantity=cart_product.Quantity
            )
        
        # Clear the cart after order creation
        cart_products.delete()

        # Redirect to a confirmation or payment page
        return redirect('order_confirmation', order_id=new_order.Order_ID)

    context = {
        'cart_products': cart_products,
        'total_price': cart.total_price,
    }

    return render(request, 'checkout.html', context)

def order_confirmation(request, order_id):
    order = Orders.objects.get(pk=order_id)
    order_products = OrderProduct.objects.filter(Order_ID=order)

    context = {
        'order': order,
        'order_products': order_products
    }
    
    return render(request, 'order_confirmation.html', context)


@login_required
def process_payment(request, order_id):
    order = get_object_or_404(Orders, Order_ID=order_id)

    if request.method == 'POST':
        payment = Payment.objects.create(
            CustomerID=request.user,
            Order_ID=order,
            Amount=order.Total_Price,
            Method=request.POST['payment_method']
        )
        
        order.Status = 'Paid'
        order.save()

        return redirect('payment_success')  # Redirect to a payment success page

    return render(request, 'payment.html', {'order': order})
