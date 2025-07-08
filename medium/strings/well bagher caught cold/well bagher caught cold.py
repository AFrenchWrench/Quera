# link https://quera.org/problemset/1023

answers = []
for i in range(1, 6):
    word = input()
    if ("HAFEZ" in word) or ("MOLANA" in word):
        found = True
        answers.append(str(i))
if answers:
    print(" ".join(answers))
else:
    print("NOT FOUND!")
