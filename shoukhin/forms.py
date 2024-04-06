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

