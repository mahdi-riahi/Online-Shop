from django import template

from products.templatetags.product_tags import toman_price

register = template.Library()

register.filter('toman', toman_price)


@register.filter
def get_item_price(product, quantity):
    return quantity * product.price
