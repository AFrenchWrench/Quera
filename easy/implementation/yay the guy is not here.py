# link https://quera.org/problemset/3538

days_in_list = []

for _ in range(3):
    days = int(input())
    days_in_list += input().split()

days_in_set = set(days_in_list)

print(7 - len(days_in_set))
