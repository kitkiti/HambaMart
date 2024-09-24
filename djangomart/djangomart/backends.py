# djangomart/backends.py

from django.contrib.auth.backends import BaseBackend
from apps.customers.models import Customer
from apps.products.models import Admin

class CustomerBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            customer = Customer.objects.get(Email=username)
            if customer.check_password(password):
                return customer
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None

class AdminBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            admin = Admin.objects.get(Email=username)
            if admin.check_password(password):
                return admin
        except Admin.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Admin.objects.get(pk=user_id)
        except Admin.DoesNotExist:
            return None