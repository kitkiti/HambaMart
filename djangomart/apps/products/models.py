from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AdminManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Admin(AbstractBaseUser, PermissionsMixin):
    AdminID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=True, null=True)
    Email = models.EmailField(unique=True, max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = AdminManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Name']

    class Meta:
        db_table = 'admin'

class Product(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    Stock = models.IntegerField(blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.CharField(max_length=255, blank=True, null=True, default='https://linklog.com/wp-content/uploads/2023/08/no-image.jpg')
    AdminID = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True, db_column='AdminID')

    class Meta:
        managed = False
        db_table = 'product'

    @property
    def tags(self):
        return ProductTags.objects.filter(Product_ID=self)


class ProductTags(models.Model):
    id = models.AutoField(primary_key=True)
    Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='Product_ID')
    Tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_tags'
        unique_together = (('Product_ID', 'Tag'),)