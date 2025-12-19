# link https://quera.org/problemset/616

from math import floor, log2

n = int(input())
i = floor(log2(n)) + 1
print(2**i)
