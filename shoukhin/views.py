from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
def logoutUser(request):
    logout(request)
    return redirect('home')


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
    cart_items = Cart.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    #total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'body/cart.html', context=context)


def add_to_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=prod,
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')


def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {
        'order': order,
    }

    return  render(request,template_name='body/orders.html',context=context)

def add_orders(request):
    if request.method =='POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        # Get the product ID from the query parameters
        product_id = request.GET.get('product_id')
        if product_id:
            # Retrieve the product object based on the ID
            product_obj = get_object_or_404(product, pk=product_id)
            # Pre-fill the form with product details
            initial_data = {
                'product': product_obj,
                'total_amount': product_obj.price,
            }
            form = orderForm(initial=initial_data)
        else:
            form = orderForm()

    context = {
        'form': form
    }
    return render(request, template_name='body/orderForm.html', context=context)
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

@login_required
def userProfile_add(request):

    if request.method == 'POST':
        form = userProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.username = request.user.username  # Prefill username
            form.save()
            return redirect('home')
    else:
        # Prefill the username field with the username of the logged-in user
        form = userProfileForm(initial={'username': request.user.username})

    context = {
        'form': form
    }
    return render(request, 'body/profileForm.html', context=context)


def user_view(request):
    try:
        profile = userProfile.objects.get(user=request.user)
    except userProfile.DoesNotExist:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, 'body/user.html', context=context)


def edit_profile(request):
    profile_instance = request.user.userprofile
    form = userProfileForm(instance=profile_instance)

    if request.method == 'POST':
        form = userProfileForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            form.save()
            return redirect('user')  # Redirect to the profile page after editing

    context = {
        'form': form
    }
    return render(request, 'body/profileForm.html', context=context)


def add_rating(request):
    # Get the order ID and product name from the query parameters
    order_id = request.GET.get('order_id')
    product_name = request.GET.get('product_name')

    print("Order ID:", order_id)
    print("Product Name:", product_name)

    if request.method == 'POST':
        form = ratingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        # Get the product object based on the name
        product_obj = get_object_or_404(product, name=product_name)

        # Pre-fill the form with order and product details
        initial_data = {
            'order': order_id,
            'product': product_obj.pk,  # Use the product object's primary key
        }
        print("Initial Data:", initial_data)  # Print initial data for debugging
        form = ratingForm(initial=initial_data)

    context = {
        'form': form
    }
    return render(request, 'body/add_rating.html', context)

def product_rating(request,id):
    rate = Rating.objects.filter(product_id= id)
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

def category_cloth(request):
    pro = product.objects.all()
    context={
        'product':pro,
    }
    return  render(request,template_name='body/category_cloth.html',context=context)

def category_nakshi_kantha(request):
    pro = product.objects.all()
    context={
        'product':pro,
    }
    return  render(request,template_name='body/category_nakshi_kantha.html',context=context)