# link https://quera.org/problemset/4065

a, b, l = map(int, input().split())
half = l // 2
time = a * (l - half) + b * half
print(time)
