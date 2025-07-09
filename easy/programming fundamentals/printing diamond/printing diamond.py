# link https://quera.org/problemset/618


def print_diamond(n):
    ranges = list(range(n + 1)) + list(range(n - 1, -1, -1))
    for i in ranges:
        print(" " * (n - i) + "*" * (2 * i + 1))


n = int(input())
print_diamond(n)
