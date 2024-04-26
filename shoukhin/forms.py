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

class createAccForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ['username','password1','password2','nid','name','email','contact_no','address','account_type','picture','about_myself']
