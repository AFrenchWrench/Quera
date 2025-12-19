# link https://quera.org/problemset/280

a, b, c = sorted(int(input()) for _ in range(3))
print("YES" if a**2 + b**2 == c**2 else "NO")
