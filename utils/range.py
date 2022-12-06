class Range:
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y

    def __str__(self):
        return "({0}-{1})".format(self.X, self.Y)

    def __eq__(self, other):
        return other.X == self.X and other.Y == self.Y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(f"{self.X},{self.Y}")

    def contains(self, r) -> bool:
        return self.X <= r.X and self.Y >= r.Y

    def contains_point(self, p) -> bool:
        return self.X <= p and p <= self.Y
    
    def overlaps(self, r) -> bool:
        return self.contains_point(r.X) or self.contains_point(r.Y) or r.contains(self)