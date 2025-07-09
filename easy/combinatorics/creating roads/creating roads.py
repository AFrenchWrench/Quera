# link https://quera.org/problemset/2637

import math

roads = int(input())
divs = int((math.ceil(roads / 2) + 1) * (math.floor(roads / 2) + 1))
print(divs)
