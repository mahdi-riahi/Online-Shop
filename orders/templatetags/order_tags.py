from django import template

register = template.Library()


@register.simple_tag
def filter_by_status(orders, *statuses):
    return orders.filter(status__in=statuses)
