from django.db import models

# Create your models here.
class Admin(models.Model):
    AdminID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)

class Product(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Stock = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.CharField(max_length=255)
    AdminID = models.ForeignKey(Admin, on_delete=models.CASCADE)

class ProductTags(models.Model):
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Tag = models.CharField(max_length=255)
    class Meta:
        unique_together = (('Product_ID', 'Tag'),)