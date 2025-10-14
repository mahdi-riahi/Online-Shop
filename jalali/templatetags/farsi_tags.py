from django import template

register = template.Library()


def toman_price(value):  # value can be int or str
    digits = str(value)
    reversed_digits = digits[::-1]

    chunks = [reversed_digits[i:i + 3] for i in range(0, len(reversed_digits), 3)]
    result = ','.join(chunks)[::-1]
    return result


register.filter('toman', toman_price)


@register.filter
def number_farsi(value):
    str_num = str(value)
    e_t_p_translate = str_num.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return str_num.translate(e_t_p_translate)
    # farsi_digits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
    # result = ''
    # for i in str_num:
    #     if i.isdigit():
    #         result += farsi_digits[int(i)]
    #     else:
    #         result += i
    # return result
