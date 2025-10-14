from django import template
import re

register = template.Library()


@register.filter
def capitalize_sentences(value):
    sentences = re.split(r'([.!?]+\s*)', value)
    result = []
    capitalize_next = True

    for part in sentences:
        if capitalize_next and part.strip():
            for i, char in enumerate(part):
                if char.isalpha():
                    part = part[:i] + char.upper() + part[i + 1:]
                    break
            capitalize_next = False
        result.append(part)

        if part.strip() and part.rstrip()[-1] in '.!?':
            capitalize_next = True

    return ''.join(result)
