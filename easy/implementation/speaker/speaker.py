# link https://quera.org/problemset/3430

word = input()
for i in range(len(word)):
    word = (word[i] * (i + 1)) + word[i + 1 :]
    print(word)
