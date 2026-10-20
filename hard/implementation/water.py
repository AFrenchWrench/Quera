# link https://quera.org/problemset/8527

# May have a better solution ( Something faster )

n = int(input())
heights = list(map(int, input().split()))

total_water = 0

stack = []
for i in range(n):
    if stack == []:
        stack.append(heights[i])
        continue

    if heights[i] >= stack[0]:
        while stack != []:
            total_water += stack[0] - stack.pop()

    stack.append(heights[i])

n = len(stack)
if n >= 3:
    stack.reverse()
    heights = stack.copy()

    stack = []
    for i in range(n):
        if stack == []:
            stack.append(heights[i])
            continue

        if heights[i] >= stack[0]:
            while stack != []:
                total_water += stack[0] - stack.pop()

        stack.append(heights[i])

print(total_water)
