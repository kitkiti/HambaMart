
"""
URL configuration for djangomart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #new
from apps.products  import views as pviews
from apps.customers import views as cviews
from django.urls import path
from apps.orders import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pviews.home, name='home'),
    path('login/', cviews.custom_login_view, name='login'),
    path('base/', pviews.base, name='base'),
    path('signup/', cviews.signup_view, name='signup'),
    # path('my_account/', cviews.account_view, name='account'),

    path('admin_dashboard/', pviews.admin_dashboard, name='admin_dashboard'),
    path('logout/', cviews.logout_view, name='logout'),
    path('cart/', cviews.cart_view, name='cart'),
    path('product/<int:product_id>/', pviews.product_details_view, name='product_details'),
    path('search/', pviews.product_search, name='product_search'),

    path('edit_product/', pviews.editproduct_view, name='edit_product'),
    path('deleteproduct_view/', pviews.deleteproduct_view, name='deleteproduct_view'),
    path('add_product/', pviews.add_product_view, name='add_product_view'),
    path('search-edit-product/', pviews.search_and_edit_product, name='search_and_edit_product'),

    path('add_to_cart/<int:product_id>/', cviews.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_id>/<int:product_id>/', cviews.remove_from_cart, name='remove_from_cart'),

    path('checkout/', order_views.checkout, name='checkout'),
    path('process_payment/<int:order_id>/', order_views.process_payment, name='process_payment'),
    path('order_confirmation/<int:order_id>/', order_views.order_confirmation, name='order_confirmation'),
    # path('payment_success/', order_views.payment_success, name='payment_success'),
    path('product_delete/', pviews.product_delete_view, name='product_delete'),
    path('account', cviews.profile_view, name='account'),
    path('payment-success/', order_views.payment_success, name='payment_success'),
]
