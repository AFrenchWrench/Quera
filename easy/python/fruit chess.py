# link https://quera.org/problemset/60134


def fruits(tuple_of_fruits):
    good_fruits = {}

    for fruit_detail in tuple_of_fruits:
        is_sphere = fruit_detail["shape"] == "sphere"
        is_in_mass_range = 300 <= fruit_detail["mass"] <= 600
        is_in_volume_range = 100 <= fruit_detail["volume"] <= 500

        is_valid = all((is_sphere, is_in_mass_range, is_in_volume_range))

        if is_valid:
            name = fruit_detail["name"]
            if name in good_fruits.keys():
                good_fruits[name] += 1
            else:
                good_fruits[name] = 1

    return good_fruits
