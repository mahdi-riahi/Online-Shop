from django.contrib import admin

from .models import Product,Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('-datetime_modified', '-price')
    list_display = ('title', 'price', 'active', 'datetime_modified', )


class CommentAdmin(admin.ModelAdmin):
    ordering = ('-datetime_modified', )
    list_display = ('author', 'product', )


admin.site.register(Comment, CommentAdmin)
