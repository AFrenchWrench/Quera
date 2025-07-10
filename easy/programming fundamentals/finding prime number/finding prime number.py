# link https://quera.org/problemset/593


def is_prime(n):
    if n == 1 or (n % 2 == 0 and n != 2):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = input()
digits_sum = sum(map(int, list(num)))
num = int(num)

while digits_sum != 0:
    num += 1
    if is_prime(num):
        digits_sum -= 1
print(num)
