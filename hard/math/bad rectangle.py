# link https://quera.org/problemset/3541

"""

To understand why this question was labeled as hard, let me explain how we
get to this code.

We have 3 basic rules:

x + y + z = n
and
x <= y <= z
and
x + y > z

and we should count the unique x,y,z sets that fit the rules.

with a bit of playing we can stablish that:

1 <= x <= n//3
((n - 2x) / 2) < y <= ((n - x) / 2)
ceil(n/3) <= z < n/2

since z = n - x - y by knowing n, x and y we get z.
so counting z in the calculations is unnecessary.

since we are given n. we can create the range for x and with that create a range for y.

so if n = 12

we know 1 <= x <= 4
so for each x, we have a range for y:

x = 1 : ((12 - 2) / 2) < y <= ((12 - 1) / 2) -> 5 < y <= 5.5
which gives zero valid answers

x = 2 : ((12 - 4) / 2) < y <= ((12 - 2) / 2) -> 4 < y <= 5
which gives one valid answer: (x = 2, y = 5, z = 5)

x = 3 : ((12 - 6) / 2) < y <= ((12 - 3) / 2) -> 3 < y <= 4.5
which gives one valid answer: (x = 3, y = 4, z = 5)

x = 4 : ((12 - 8) / 2) < y <= ((12 - 4) / 2) -> 2 < y <= 4
which gives two valid answers: (x = 4, y = 3, z = 5) and (x = 4, y = 4, z = 4)
but y = 3 is not valid because we had x <= y. hence we have only one valid answer here

so we calculated the unique sets that follow the 3 rules with the given n.

"""

n = int(input())

total = 0

for x in range(1, n // 3 + 1):
    upper = (n - x) // 2
    lower = max(x - 1, (n - 2 * x) // 2)
    total += upper - lower

print(total)
