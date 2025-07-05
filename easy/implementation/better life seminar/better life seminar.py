# link https://quera.org/problemset/10325

row, sit = map(int, input().split())

direction = "Right" if sit <= 10 else "Left"
sit_from_entrance = sit if sit <= 10 else 21 - sit
row_from_top = 11 - row

print(direction, row_from_top, sit_from_entrance)
