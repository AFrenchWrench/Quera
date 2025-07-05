# link https://quera.org/problemset/3539

# normal way using loops and type casting
num = input()
while len(num) > 1:
    num = str(sum(map(int, num)))
print(num)

# digital root formula
# def digital_root(n):
#     return 0 if n == 0 else (n - 1) % 9 + 1
# print(digital_root(int(input())))
