from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.customers.models import Customer

class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['FName', 'LName', 'Email', 'Phone', 'password1', 'password2']