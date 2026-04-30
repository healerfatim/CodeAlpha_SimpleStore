from django.contrib import admin

# Register your models here.

# Import the Product model you created in models.py
from .models import Product 

# This line tells Django to show "Products" in the admin panel
admin.site.register(Product)
