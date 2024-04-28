from ..models import Post


def generate(title):
    title = title.lower().strip().replace(" ", "-")
    if Post.objects.filter(slug=title).exists:
        count = int_to_roman(Post.objects.filter(slug=title).count())
        return f"{title}-{count}"
    return title


def int_to_roman(n):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    thousands = m[n // 1000]
    hundreds = c[(n % 1000) // 100]
    tens = x[(n % 100) // 10]
    ones = i[n % 10]

    return (thousands + hundreds + tens + ones)
