# link https://quera.org/problemset/35253

num = input()
weights = list(map(int, input().split()))

print((weights.index(max(weights)) + 1))
