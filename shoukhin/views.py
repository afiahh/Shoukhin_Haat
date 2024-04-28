from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
# Create your views here.
def home_page(request):
    return render(request,template_name='body/dashboard.html')

#def dashboard(request):
    #  return  render(request,template_name='body/dashboard.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request,template_name='body/login.html')

def createAcc(request):
    form = createAccForm()
    if request.method == 'POST':
        form = createAccForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile is created.")
            return redirect('login')
    context = {
        'form': form
    }
    return render(request,template_name='body/createAcc.html',context=context)

def cart(request):
    return  render(request,template_name='body/cart.html')

def orders(request):
    return  render(request,template_name='body/orders.html')

def product_details(request):
    pro = product.objects.all()
    context={
        'product':pro,
    }
    return  render(request,template_name='body/product_details.html',context=context)

def add_product(request):
    form=productForm()
    if request.method =='POST':
        form=productForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_details')

    context={
        'form': form
    }
    return render(request, template_name='body/add_product.html',context=context)

def edit_product(request,id):
    prod = product.objects.get(pk=id)
    form=productForm(instance=prod)
    if request.method == 'POST':
        form=productForm(request.POST,request.FILES , instance=prod)
        if form.is_valid():
            form.save()
            return redirect('product_details')

    context = {
        'form': form
    }
    return render(request, template_name='body/add_product.html', context=context)

def delete_product(request,id):
   prod = product.objects.get(pk=id)
   if request.method == 'POST':
    prod.delete()
   return redirect('product_details')

def view_product(request,id):
    prod=product.objects.get(pk=id)
    context = {
        'product': prod,
    }
    return render(request, template_name='body/view_product.html',context=context)


def seller(request):
    return  render(request,template_name='body/seller.html')

def add_rating(request):
    form=ratingForm
    if request.method =='POST':
        form=ratingForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_rating')

    context={
        'form': form
    }
    return render(request, template_name='body/add_rating.html',context=context)

def product_rating(request):
    rate = Rating.objects.all()
    context={
        'Rating':rate,
    }
    return  render(request,template_name='body/product_rating.html',context=context)

def buyer(request):
    return  render(request,template_name='body/buyer.html')


def your_view_function(request):
    # Your view logic here
    context = {
        'request': request
    }
    return render(request, template_name='body/navbar.html', context=context)

def category_jute(request):
    pro = product.objects.all()
    context={
        'product':pro,
    }
    return  render(request,template_name='body/category_jute.html',context=context)

def category_nakshi_kantha(request):
    pro = product.objects.all()
    context={
        'product':pro,
    }
    return  render(request,template_name='body/category_nakshi_kantha.html',context=context)