from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


class CommentInline(admin.StackedInline):  # or TabularInline
    model = Comment
    fields = ['author', 'text', 'active', 'stars', 'recommendation', ]
    extra = 5


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    ordering = ('-datetime_modified', '-price')
    list_display = ('title', 'price', 'active', 'datetime_modified', )
    # inline
    inlines = [
        CommentInline,
    ]


class CommentAdmin(admin.ModelAdmin):
    ordering = ('-datetime_modified', )
    list_display = ('author', 'product', )


admin.site.register(Comment, CommentAdmin)
