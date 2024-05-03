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
    path('/login/home/', s_view.loginpage, name='login'),
    path('/logout/', s_view.logoutUser, name='logout'),
    path('/login/createAcc/', s_view.createAcc, name='createAcc'),
    path('/cart/', s_view.cart, name='cart'),
    path('add-to-cart/<int:product_id>/',s_view.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', s_view.remove_from_cart, name='remove_from_cart'),
    #path('cart/', view_cart, name='cart'),
    path('/orders/', s_view.orders, name='orders'),
    path('orderForm/', s_view.add_orders, name='orderForm'),
    path('/product_details/', s_view.product_details, name='product_details'),
    #path('dashboard', s_view.dashboard, name='dashboard'),
    path('product_details/', s_view.product_details, name='product_details'),
    path('product_details/<str:id>', s_view.view_product, name='view_product'),
    path('buyer/', s_view.buyer, name='buyer'),
    path('user/', s_view.user_view, name='user'),
    path('profileForm/', s_view.userProfile_add, name='profileForm'),
    path('profileForm/edit_profile/', s_view.edit_profile, name='edit_profile'),
    path('product_details/add_product/',s_view.add_product, name='add_product'),
    path('product_details/edit_product/<str:id>', s_view.edit_product, name='edit_product'),
    path('product_details/delete_product/<str:id>/', s_view.delete_product, name='delete_product'),
    path('add_rating/',s_view.add_rating, name='add_rating'),
    path('add_rating/product_rating/<int:id>/', s_view.product_rating, name='product_rating'),
    path('category_jute/',s_view.category_jute, name='category_jute'),
    path('category_cloth/',s_view.category_cloth, name='category_cloth'),
    path('category_nakshi_kantha/',s_view.category_nakshi_kantha, name='category_nakshi_kantha'),
]

urlpatterns+= static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
