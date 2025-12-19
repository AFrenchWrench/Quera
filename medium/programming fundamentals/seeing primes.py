# link https://quera.org/problemset/649


def is_prime(n):
    if n == 1 or (n != 2 and n % 2 == 0):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num1 = int(input())
num2 = int(input())

prime_list = []
for i in range(num1 + 1, num2):
    if is_prime(i):
        prime_list.append(str(i))
print(",".join(prime_list))
