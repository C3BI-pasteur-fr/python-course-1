class Coordinate

    def __init__(self, x, y):
        self.set_coord(x, y)

    def _check_coord(self, val):
        return isinstance(int, val) and val >=0


    @property
    def coord(self):
        return (self._x, self._y)


    @coord.setter
    def coord(self, coord):
        x, y = coord
        if self._check_coord(x):
            self._x = x
        else:
            raise ValueError("x must be a positive integer")
        if self._check_coord(y):
            self._y = y
        else:
            raise ValueError("y must be a positive integer")


a = Coordinate(2, 3)
a.coord
a.coord = 3, 4