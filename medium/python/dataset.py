# link https://quera.org/problemset/190993

n, q, l = map(int, input().split())

known_codes = {}

for _ in range(n):
    code, label = input().split()
    known_codes[code] = label

for _ in range(q):
    code = input()
    print(known_codes.get(code, "Unknown"))
