# link https://quera.org/problemset/251440

a, b, c = list(map(int, input().split("?")))

result = max((a + b) + c, (a + b) * c, a * (b + c), a * b * c)

print(result)
