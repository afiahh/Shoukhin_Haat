from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([product,Cart,Order,Rating,userProfile])