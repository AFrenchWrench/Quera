# link https://quera.org/problemset/3410


def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)
    return triangle


n = int(input())

triangle = generate_pascals_triangle(n)
for row in triangle:
    print(" ".join(map(str, row)))
