from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    Cart_ID = models.IntegerField(primary_key=True)  # Ensuring Cart_ID matches CustomerID
    CustomerID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='CustomerID')
    total_price = models.IntegerField(default=0)


    class Meta:
        db_table = 'cart'
        unique_together = (('Cart_ID', 'CustomerID'),)



class CartProduct(models.Model):

    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='Product_ID')
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerID')
    Cart_ID = models.ForeignKey(Cart, on_delete=models.CASCADE, db_column='Cart_ID')
    Quantity = models.IntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    class Meta:
        db_table = 'cart_product'

