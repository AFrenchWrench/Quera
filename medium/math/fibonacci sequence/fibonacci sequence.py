# link https://quera.org/problemset/17675


def fib_up_to(n):
    fibs = [1, 2]
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


n = int(input())
if n == 1:
    print("+")
else:
    fibs = fib_up_to(n)

    output = ["-"] * n
    for i in fibs:
        output[i - 1] = "+"

    print("".join(output))
