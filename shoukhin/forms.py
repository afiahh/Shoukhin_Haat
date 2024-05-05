from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class productForm(ModelForm):
    class Meta:
        model=product
        fields='__all__'

class ratingForm(ModelForm):
    class Meta:
        model=Rating
        fields='__all__'

class orderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class createAccForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class userProfileForm(ModelForm):
    class Meta:
        model=userProfile
        fields = '__all__'
