# link https://quera.org/problemset/87181

import re

non_alpha = re.compile(r"[^a-zA-Z]")


def words_check(text: str):
    words = text.split()
    good_words = {}

    for word in words:
        good_word = re.sub(non_alpha, "", word).capitalize()

        if len(good_word) <= (len(word) / 2):
            continue

        if good_word not in good_words:
            good_words[good_word] = 1
        else:
            good_words[good_word] += 1

    return good_words
