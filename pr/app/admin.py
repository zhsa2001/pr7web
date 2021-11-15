from django.contrib import admin

# Register your models here.
from .models import Product

#admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'date_of_last_delivery')
    list_filter = ('date_of_last_delivery','quantity')

admin.site.register(Product, ProductAdmin)
