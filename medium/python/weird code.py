# link https://quera.org/problemset/16396


class Foo:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value >= 0:
            value %= 100
        else:
            value = -1

        self._x = value
