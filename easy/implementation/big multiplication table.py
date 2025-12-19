# link https://quera.org/problemset/3409

multiplication_num = int(input())
for i in range(1, multiplication_num + 1):
    for j in range(1, multiplication_num + 1):
        print(i * j, end=" ")
    print()
