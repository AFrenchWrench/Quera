# link https://quera.org/problemset/108665

VOWELS = ("a", "e", "i", "o", "u")


def count_vowels(word):
    count = 0
    for char in word:
        if char in VOWELS:
            count += 1
    return count


print(2 ** count_vowels(input()))
