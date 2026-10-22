# link https://quera.org/problemset/129728

# I formatted the code for readability, the submitted file should be 1 line only
print(
    " ".join(
        sorted(
            [x if (((ord(x) - 97) % 2) == 0) else x.upper() for x in input()],
            reverse=True,
        )
    )
)
