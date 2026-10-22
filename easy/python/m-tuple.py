# link https://quera.org/problemset/76278


def calculator(n, m, li):
    value = 0
    sign = 1
    for i in range((n // m) + 1):
        value += sum(li[i * m : (i + 1) * m]) * sign
        sign *= -1

    return value
