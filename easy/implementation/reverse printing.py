# link https://quera.org/problemset/3405

# mind you that this works on python 3.8+
nums = []
while (n := int(input())) != 0:
    nums.append(n)
print(*reversed(nums), sep="\n")
