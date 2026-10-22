# link https://quera.org/problemset/129726


def separator(ls):
    evens = []
    odds = []

    for num in ls:
        evens.append(num) if num % 2 == 0 else odds.append(num)

    return evens, odds
