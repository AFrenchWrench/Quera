# link https://quera.org/problemset/2886

hours, mins = map(int, input().split())

if hours != 0:
    hours = 12 - hours
if mins != 0:
    mins = 60 - mins

print(f"{hours:02d}:{mins:02d}")
