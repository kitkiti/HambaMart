from django.shortcuts import render

# Create your views here.
# products/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def admin_view(request):
    return render(request, 'admin_dashboard.html')

