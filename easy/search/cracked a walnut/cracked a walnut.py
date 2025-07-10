# link https://quera.org/problemset/3540

import sys


distance, x, y = map(int, input().split())
x_count = y_count = 0

if distance % x == 0:
    print(int(distance / x), 0)
elif distance % y == 0:
    print(0, int(distance / y))
else:
    while True:
        distance -= y
        y_count += 1
        if distance % x == 0 and distance > 0:
            x_count = int(distance / x)
            break
        elif distance < 0:
            print(-1)
            sys.exit()
    print(x_count, y_count)
