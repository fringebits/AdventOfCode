class Grid:
    def __init__(self, width, height, fill = None):
        self.width = width
        self.height = height
        self.data = []
        if fill is not None:
            self.data = [fill for x in range(self.width * self.height)]

    def contains(self, pos):
        return pos.X >= 0 and pos.X < self.width and pos.Y >= 0 and pos.Y < self.height

    def get(self, row, col):
        index = col + row * self.width
        return self.data[index]

    def set(self, row, col, value):
        index = col + row * self.width
        self.data[index] = value

    def get_row(self, row):
        ii = row * self.width
        return self.data[ii : ii+self.width]

    def get_col(self, col):
        result = []
        for ii in range(self.height):
            result.append(self.data[col + ii * self.width])
        return result

    def IndexToPos(self, index):
        return utils.Vec2(index % self.width, int(index / self.width))
    
    def PosToIndex(self, pos):
        return pos.X + pos.Y * self.width

    def GetValueAt(self, pos):
        if not self.contains(pos):
            return None
        index = self.PosToIndex(pos)
        return self.data[index]

    def __str__(self) -> str:
        result = ''
        for rr in range(0,self.height):
            result = result + self.get_row(rr).__str__() + '\n'
        return result

class HeightMap(Grid):
    def __init__(self, input):
        width = len(input[0])
        height = len(input)
        super().__init__(width, height)
        for row in input:
            self.data += [int(x) for x in row]

