# link https://quera.org/problemset/10230

x, y, z = map(int, input().split())
if all((x != 0, y != 0, z != 0, x + y + z == 180)):
    print("Yes")
else:
    print("No")
