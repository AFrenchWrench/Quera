# link https://quera.org/problemset/3406

num1 = input()
num2 = input()

rev1 = int(num1[::-1])
rev2 = int(num2[::-1])

if rev1 > rev2:
    print(num2, "<", num1)
elif rev1 < rev2:
    print(num1, "<", num2)
else:
    print(num1, "=", num2)
