class Vec3:
    def __init__(self, x, y, z) -> None:
        self.X = x
        self.Y = y
        self.Z = z

    def __str__(self):
        return f"({self.X},{self.Y},{self.Z})"

    def __add__(self, other):
        x = self.X + other.X
        y = self.Y + other.Y
        z = self.Z + other.Z
        return Vec3(x, y, z)

    def __eq__(self, other):
        return other.X == self.X and other.Y == self.Y and other.Z == self.Z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(f"{self}")