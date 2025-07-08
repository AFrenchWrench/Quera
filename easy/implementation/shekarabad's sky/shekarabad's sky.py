# link https://quera.org/problemset/6082

rows, cols = map(int, input().split())
stars_count = 0

for _ in range(rows):
    row = input()
    stars_count += row.count("*")

print(stars_count)
