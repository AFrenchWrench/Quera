# link https://quera.org/problemset/49535

bottles_count, liquid = map(int, input().split())

bottles_volume = 0
for _ in range(bottles_count):
    volume = int(input())
    bottles_volume += volume

if bottles_volume >= liquid:
    print("YES")
else:
    print("NO")
