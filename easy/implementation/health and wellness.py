# link https://quera.org/problemset/51865

score = int(input())
days = int(input())
if days == 0:
    print(20)
elif days == 7:
    print(score)
else:
    print(max(0, score - days))
