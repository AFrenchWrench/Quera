# link https://quera.org/problemset/102250


def find(num1, num2, num3):
    s1 = set(range(1, 5))
    s2 = {num1, num2, num3}

    return (s1 - s2).pop()
