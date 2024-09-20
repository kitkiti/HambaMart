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

    class Meta:
        managed = False
        db_table = 'orders'

class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    Product_ID = models.ForeignKey(Product, on_delete=models.RESTRICT)
    Order_ID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_product'
        unique_together = (('Product_ID', 'Order_ID'),)

class Payment(models.Model):
    P_ID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    Order_ID = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Method = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'