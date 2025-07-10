# link https://quera.org/problemset/33045

num = int(input())

nums_count = 0
nums_sum = 0
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            nums_count += 1
            nums_sum += j
print(nums_count, nums_sum)
