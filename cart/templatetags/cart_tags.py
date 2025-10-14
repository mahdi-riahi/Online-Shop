from django import template

register = template.Library()


@register.filter
def get_item_price(product, quantity):
    return quantity * product.price
