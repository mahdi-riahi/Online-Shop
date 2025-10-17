from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1
    fields = ['order', 'product', 'quantity', 'price', ]


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, ]
    list_display = ['user', 'status', 'is_paid']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'quantity']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
