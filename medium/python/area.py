# link https://quera.org/problemset/33473

# remove the type hints before submitting

from math import pi


def square(x: int | float):
    return x * x


def circle(r: int | float):
    return r * r * pi


def rectangle(x: int | float, y: int | float):
    return x * y


def triangle(h: int | float, x: int | float):
    return h * x / 2


def get_func(ls: list[str]):
    callable_map = {
        "square": square,
        "circle": circle,
        "rectangle": rectangle,
        "triangle": triangle,
    }

    return [callable_map[shape] for shape in ls]
