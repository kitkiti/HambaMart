from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from apps.customers.models import Customer  # Import your Customer model
from apps.products.models import Admin  # Import your Admin model


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

def cart_view(request):
    return render(request, 'cart.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # Redirect to home page after logout