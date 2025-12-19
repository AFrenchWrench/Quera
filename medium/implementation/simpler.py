# link https://quera.org/problemset/3403

nums = []

for i in range(4):
    nums.append(int(input()))

sum_nums = sum(nums)
average = sum_nums / 4
product = 1
for i in nums:
    product *= i

print("Sum : {:.6f}".format(sum_nums))
print("Average : {:.6f}".format(average))
print("Product : {:.6f}".format(product))
print("MAX : {:.6f}".format(max(nums)))
print("MIN : {:.6f}".format(min(nums)))
