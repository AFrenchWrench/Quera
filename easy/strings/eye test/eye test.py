# link https://quera.org/problemset/2659

num = int(input())
test = input()
answers = input()

wrong_answers = 0
for t, a in zip(test, answers):
    if t != a:
        wrong_answers += 1
print(wrong_answers)
