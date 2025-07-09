# link https://quera.org/problemset/2529

name_count = int(input())
max_uniqueness = 0

for _ in range(name_count):
    name = input()
    unique_char_count = len(set(name))
    if unique_char_count > max_uniqueness:
        max_uniqueness = unique_char_count
print(max_uniqueness)
