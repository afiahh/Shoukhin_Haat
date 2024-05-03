from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],blank=True, null=True)
    review = models.TextField(max_length=400,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} stars by {self.user} for {self.product.name}"

class product(models.Model):

    CATEGORY_CHOICES = CATEGORY_CHOICES = [
        ('jute', 'Jute'),
        ('clothing', 'Clothing'),
        ('jewellery', 'Jewellery'),
        ('food', 'Food'),
        ('home_decor', 'Home Decor'),
        ('pottery', 'Pottery'),
        ('nakshi_kantha', 'Nakshi Kantha'),
        ('others', 'Others'),
    ]
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    measurements = models.CharField(max_length=300)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='others')
    image = models.ImageField(upload_to='static/images', blank=True, null=True, default='static/images/default_no_img.jfif')
    stock = models.IntegerField(default=0)
    # rating = models.ForeignKey(Rating, on_delete=models.CASCADE ,blank=True,null=True)
    #review = models.ForeignKey(Rating, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.PositiveIntegerField(default=1,blank=True,null=True)

    def __str__(self):
        return f"Cart for {self.user}"

class Order(models.Model):
    STATUS_CHOICES = [

         ('pending', 'pending'),
         ('processing', 'processing'),
         ('shipped', 'shipped'),
         ('delivered', 'delivered'),
         ('cancelled', 'cancelled'),

    ]
    PAYMENT_CHOICES = [

        ('bkash', 'bkash'),
        ('COD', 'COD'),
        ('bank', 'bank'),
        ('nagad', 'nagad'),
        ('rocket', 'rocket'),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending',blank=True,null=True)
    total_amount = models.IntegerField()
    shipping_address = models.TextField(max_length=200)
    payment_method = models.CharField(max_length=30,choices=PAYMENT_CHOICES, default='COD',blank=True,null=True)

    def __str__(self):
        return f"Order {self.id} by {self.user}"


class userProfile(models.Model):
    NID_LENGTH = 20
    ACCOUNT_TYPES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    #email = models.EmailField(blank=True, null=True)
    nid = models.CharField(max_length=NID_LENGTH) #min length 10
    contact_no = models.CharField(max_length=20,blank=True, null=True,default='+880')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    picture = models.ImageField(upload_to='static/images', blank=True, null=True,default='static/images/default_no_img.jfif')
    about_myself = models.TextField(blank=True, null=True,default='will add later')
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


#class profile(models.Model):
    #user = User.OnetoON

