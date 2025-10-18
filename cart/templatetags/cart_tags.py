from django import template

register = template.Library()


@register.filter
def get_item_price(product, quantity):
    return quantity * product.price

@register.filter
def get_item_price_price_quantity(price, quantity):
    return price * quantity
