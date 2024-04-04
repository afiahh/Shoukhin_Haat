from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home_page(request):
    return render(request,template_name='body/dashboard.html')

#def dashboard(request):
    #  return  render(request,template_name='body/dashboard.html')

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

def view_product(request,id):
    prod=product.objects.get(pk=id)
    context = {
        'product': prod,
    }
    return render(request, template_name='body/view_product.html',context=context)


def seller(request):
    return  render(request,template_name='body/seller.html')

def buyer(request):
    return  render(request,template_name='body/buyer.html')


def your_view_function(request):
    # Your view logic here
    context = {
        'request': request
    }
    return render(request, template_name='body/navbar.html', context=context)
