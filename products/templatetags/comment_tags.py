from django import template


register = template.Library()


@register.filter
def active_comments(comments):
    return comments.exclude(active=False)


@register.filter
def order_by_datetime_comments(comments):
    return comments.order_by('-datetime_created')
