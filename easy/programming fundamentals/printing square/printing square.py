# link https://quera.org/problemset/591

num = int(input())
for i in range(1, num + 1):
    if i == num or i == 1:
        print("*" * num)
    else:
        print("*" + " " * (num - 2) + "*")
