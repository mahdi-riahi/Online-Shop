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


def toman_price(value):
    digits = str(value)
    reversed_digits = digits[::-1]

    chunks = [reversed_digits[i:i + 3] for i in range(0, len(reversed_digits), 3)]
    result = ','.join(chunks)[::-1]

    return result


register.filter('toman', toman_price)
