# link https://quera.org/problemset/282

n = int(input())
z = sum(i for i in range(1, n) if n % i == 0)
print("YES" if z == n else "NO")
