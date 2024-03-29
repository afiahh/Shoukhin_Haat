from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,template_name='body/dashboard.html')

#def dashboard(request):
    #return  render(request,template_name='body/dashboard.html')

def cart(request):
    return  render(request,template_name='body/cart.html')

def orders(request):
    return  render(request,template_name='body/orders.html')

def product_details(request):
    return  render(request,template_name='body/product_details.html')

def seller(request):
    return  render(request,template_name='body/seller.html')

def buyer(request):
    return  render(request,template_name='body/buyer.html')
