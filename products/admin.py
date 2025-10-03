from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('-datetime_modified', '-price')
    list_display = ('title', 'price', 'active', 'datetime_modified', )
