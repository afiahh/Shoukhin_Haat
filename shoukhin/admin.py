from django.contrib import admin
from .models import product,Order,Cart,Rating

# Register your models here.
admin.site.register([product,Cart,Order,Rating])