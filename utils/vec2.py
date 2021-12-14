class Vec2:
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y

    def __str__(self):
        return "({0},{1})".format(self.X, self.Y)

    def __add__(self, other):
        x = self.X + other.X
        y = self.Y + other.Y
        return Vec2(x, y)

    def __eq__(self, other):
        return other.X == self.X and other.Y == self.Y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(f"{self.X},{self.Y}")