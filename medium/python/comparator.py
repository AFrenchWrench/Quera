# link https://quera.org/problemset/102248


def compare(string1: str, string2: str):
    while True:
        first_letter1, rest1 = string1[0], string1[1:]
        first_letter2, rest2 = string2[0], string2[1:]

        if first_letter1 < first_letter2:
            string1 = rest1
        elif first_letter1 > first_letter2:
            string2 = rest2
        else:
            string1 = rest1
            string2 = rest2

        if string1 == "" or string2 == "":
            break

        string1 = string1[::-1]
        string2 = string2[::-1]

    result = string1 + string2

    return result if result != "" else "Both strings are empty!"
