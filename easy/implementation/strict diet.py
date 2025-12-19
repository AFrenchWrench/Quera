# link https://quera.org/problemset/20256

health = input()

g = health.count("G")
r = health.count("R")
y = health.count("Y")

if g == 0 or r >= 3 or (r == 2 and y == 2):
    print("nakhor lite")
else:
    print("rahat baash")
