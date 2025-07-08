# link https://quera.org/problemset/9773


def print_star_row(n, i):
    ws = (n - i) // 2
    print(f'{" " * ws}{"*" * i}{" " * (2 * ws)}{"*" * i}{" " * ws}')


n = int(input())

widths = list(range(1, n, 2)) + list(range(n, 0, -2))

for i in widths:
    print_star_row(n, i)
