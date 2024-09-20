from django.db import models
from apps.products.models import Product

# Create your models here.
class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=255)
    MName = models.CharField(max_length=255, blank=True, null=True)
    LName = models.CharField(max_length=255)
    Address = models.TextField(blank=True, null=True)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(db_column='Email', unique=True)
    Password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'

class Cart(models.Model):
    Cart_ID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cart'
        unique_together = (('Cart_ID', 'CustomerID'),)

class CartProduct(models.Model):
    id = models.AutoField(primary_key=True)
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Cart_ID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart_product'
        unique_together = (('Product_ID', 'CustomerID', 'Cart_ID'),)