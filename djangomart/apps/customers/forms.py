from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.customers.models import Customer

class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['FName', 'LName', 'Email', 'Phone', 'password1', 'password2']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['FName', 'MName', 'LName', 'Email', 'Phone', 'Address']
        widgets = {
            'Email': forms.EmailInput(attrs={'placeholder': 'Please enter your email-address'}),
            'Phone': forms.TextInput(attrs={'placeholder': 'Please enter your mobile'}),
            'Address': forms.Textarea(attrs={'placeholder': 'Please enter your home address'}),
        }        