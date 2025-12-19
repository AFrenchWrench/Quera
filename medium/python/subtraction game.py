# link https://quera.org/problemset/87176


def game(num):
    x = num % 10
    z = (num // 10) % 10
    return abs(x - z)
