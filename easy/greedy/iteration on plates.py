# https://quera.org/problemset/6375


plates = list(map(int, input().split()))

target_in_each = sum(plates) / 3

operations = 0

while not (all([(f"{x:.3f}" == f"{target_in_each:.3f}") for x in plates])):
    left_over = 0
    plates.sort()
    left_over = plates[2] - target_in_each
    if left_over == 0:
        break
    plates[2] -= left_over
    need = plates[0] - target_in_each
    plates[0] += -need
    plates[2] += left_over + need
    operations += 1

print(operations)
