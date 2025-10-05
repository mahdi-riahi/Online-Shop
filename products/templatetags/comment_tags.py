from django import template


register = template.Library()


@register.filter
def active_comments(comments):
    return comments.exclude(active=True)
