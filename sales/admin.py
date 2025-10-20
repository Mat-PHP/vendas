from django.contrib import admin
from .models import Product, Sale
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('date','product','quantity','price')
