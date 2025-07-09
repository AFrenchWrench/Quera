# link https://quera.org/problemset/80651

teams = 0
for _ in range(3):
    a = int(input())
    b = int(input())
    teams += min(a, b)
print(teams)
