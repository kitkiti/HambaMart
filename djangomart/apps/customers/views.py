from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from .models import Customer
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from djangomart.backends import CustomerBackend, AdminBackend


# Create your views here.

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Try to authenticate as Customer
            customer_user = CustomerBackend().authenticate(request, email=email, password=password)
            if customer_user is not None:
                login(request, customer_user, backend='djangomart.backends.CustomerBackend')
                return redirect('home')  # Redirect to customer dashboard

            # Try to authenticate as Admin
            admin_user = AdminBackend().authenticate(request, email=email, password=password)
            if admin_user is not None:
                login(request, admin_user, backend='djangomart.backends.AdminBackend')
                return redirect('admin_dashboard')  # Redirect to admin dashboard

            messages.error(request, 'Invalid email or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    return render(request, 'signup.html')

def account_view(request):
    return render(request, 'account.html')

def cart_view(request):
    return render(request, 'cart.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home page after logout