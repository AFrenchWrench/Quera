# link https://quera.org/problemset/91712

mouse_position, hole_position = map(int, input().split())
distance = mouse_position - hole_position

if distance > 0:
    print("L" * distance)
elif distance < 0:
    print("R" * (-distance))
else:
    print("Saal Noo Mobarak!")
