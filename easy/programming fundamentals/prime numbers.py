# link https://quera.org/problemset/293

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num1 = int(input())
num2 = int(input())
for i in range(num1, num2 + 1):
    if is_prime(i):
        print(i)
