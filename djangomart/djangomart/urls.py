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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pviews.home, name='home'),
    path('login/', cviews.custom_login_view, name='login'),
    path('base/', pviews.base, name='base'),
    path('signup/', cviews.signup_view, name='signup'),
    path('my_account/', cviews.signup_view, name='account'),

    path('admin_dashboard/', pviews.admin_view, name='admin_dashboard'),
    path('logout/', cviews.logout_view, name='logout'),
    path('cart/', cviews.cart_view, name='cart'),

]
