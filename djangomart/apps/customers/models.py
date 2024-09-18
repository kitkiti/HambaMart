from django.db import models
from apps.products.models import Product

# Create your models here.
class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=255)
    MName = models.CharField(max_length=255, blank=True, null=True)
    LName = models.CharField(max_length=255)
    Address = models.TextField()
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)

class Cart(models.Model):
    Cart_ID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('CustomerID', 'Cart_ID'),)

class CartProduct(models.Model):
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Cart_ID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    class Meta:
        unique_together = (('Product_ID', 'CustomerID', 'Cart_ID'),)