from django.db import models

# Create your models here.
class Admin(models.Model):
    AdminID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=True, null=True)
    Password = models.CharField(max_length=255)
    Email = models.EmailField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'admin'

class Product(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    Stock = models.IntegerField(blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.CharField(max_length=255, blank=True, null=True, default='https://linklog.com/wp-content/uploads/2023/08/no-image.jpg')
    AdminID = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

class ProductTags(models.Model):
    id = models.AutoField(primary_key=True)
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_tags'
        unique_together = (('Product_ID', 'Tag'),)