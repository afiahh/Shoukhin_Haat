"""
URL configuration for SHmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shoukhin import views as s_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',s_view.home_page,name = 'home'),
    path('/cart/', s_view.cart, name='cart'),
    path('/orders/', s_view.orders, name='orders'),
    path('/product_details/', s_view.product_details, name='product_details'),
    #path('dashboard', s_view.dashboard, name='dashboard'),
    path('product_details/', s_view.product_details, name='product_details'),
    path('product_details/<str:id>', s_view.view_product, name='view_product'),
    path('buyer/', s_view.buyer, name='buyer'),
    path('seller/', s_view.seller, name='seller'),
    path('product_details/add_product/',s_view.add_product, name='add_product'),
    path('product_details/edit_product/<str:id>', s_view.edit_product, name='edit_product'),
    path('product_details/delete_product/<str:id>/', s_view.delete_product, name='delete_product'),
    path('add_rating/',s_view.add_rating, name='add_rating'),
    path('add_rating/product_rating/', s_view.product_rating, name='product_rating'),
    path('category_jute/',s_view.category_jute, name='category_jute'),
    path('category_nakshi_kantha/',s_view.category_nakshi_kantha, name='category_nakshi_kantha'),
]

urlpatterns+= static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
