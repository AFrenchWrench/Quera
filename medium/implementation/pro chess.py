# link https://quera.org/problemset/2636

chess = list(map(int, input().split()))
target = [1, 1, 2, 2, 2, 8]

diffs = [t - c for c, t in zip(chess, target)]
print(*diffs)
