# link https://quera.org/problemset/34081

from math import lcm

players_count, jump = map(int, input().split())
print(lcm(players_count, jump) // jump)
