from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User  # Importing User
# Create your models here.

class CustomerManager(BaseUserManager):
    def create_user(self, Email, password=None, **extra_fields):
        if not Email:
            raise ValueError('The Email field must be set')
        Email = self.normalize_email(Email)
        user = self.model(Email=Email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(Email, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
    CustomerID = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=255)
    MName = models.CharField(max_length=255, blank=True, null=True)
    LName = models.CharField(max_length=255)
    Address = models.TextField(blank=True, null=True)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(db_column='Email', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = CustomerManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['FName', 'LName']

    class Meta:
        db_table = 'customer'


class Cart(models.Model):
    Cart_ID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerID')

    class Meta:
        managed = False
        db_table = 'cart'
        unique_together = (('Cart_ID', 'CustomerID'),)

from django.conf import settings  # Import settings to use AUTH_USER_MODEL


class CartProduct(models.Model):
    # No need to define id as AutoField, Django will automatically create it
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='ProductID', related_name='cart_products')  # Product reference with related_name
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerID')  # Renamed field for clarity
    Cart_ID = models.ForeignKey(Cart, on_delete=models.CASCADE, db_column='CartID')  # Renamed field for clarity
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product

    # Use the settings.AUTH_USER_MODEL to refer to the correct user model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_products')  # User reference with related_name

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"


    class Meta:
        managed = False
        db_table = 'cart_product'
        unique_together = (('Product_ID', 'CustomerID', 'Cart_ID'),)