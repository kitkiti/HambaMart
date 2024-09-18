from django.db import models
from apps.customers.models import Customer
from apps.products.models import Product

# Create your models here.
class Orders(models.Model):
    Order_ID = models.AutoField(primary_key=True)
    Total_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=50)
    Address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class OrderProduct(models.Model):
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Order_ID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    class Meta:
        unique_together = (('Product_ID', 'Order_ID'),)

class Payment(models.Model):
    P_ID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Order_ID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Method = models.CharField(max_length=50)