import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 20 *****")

    #lines = load_input('sample_input.txt')
    lines = load_input('input.txt')
    puzzle = Puzzle(lines)

    #assert puzzle.EnhancePixel(utils.Vec2(-2, -2)) is False

    # part 1:
    for ii in range(2):
        puzzle.Enhance()
    print(f"part1: Lights = {len(puzzle.points)}")

    # part 2:
    for ii in range(48):
        if (ii % 5) == 0:
            print(f"\tstep={ii}, Lights = {len(puzzle.points)}")
        puzzle.Enhance()
    print(f"part2: Lights = {len(puzzle.points)}")

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input

class Puzzle:
    def __init__(self, input):
        self.algorithm = input[0]

        # parse the input to create the puzzle
        self.field = False # default is the 'field is off'
        self.points = set()  # represents all the 'light' points
        yy = 0
        for line in input[2:]:
            xx = 0
            for pix in line:
                if pix == '#':
                    self.points.add(utils.Vec2(xx, yy))
                xx += 1
            yy += 1

        self.x_min, self.x_max, self.y_min, self.y_max = self.GetExtents(0)

        self.PrintBoard()

    def Enhance(self): #run one phase of image enhancement
        x_min, x_max, y_min, y_max = self.GetExtents(1)
        result = set()
        for yy in range(y_min, y_max+1):
            for xx in range(x_min, x_max+1):
                pos = utils.Vec2(xx, yy)
                pix = self.EnhancePixel(pos)
                if pix:
                    result.add(pos)
        # compute the infinite field
        pix = self.algorithm[0 if not self.field else 511]
        self.field = True if pix == '#' else False

        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.points = result
        #self.PrintBoard()

    def EnhancePixel(self, pos):
        mask = ''
        mask += self.GetValueAt(pos + utils.Vec2(-1, -1))
        mask += self.GetValueAt(pos + utils.Vec2( 0, -1))
        mask += self.GetValueAt(pos + utils.Vec2(+1, -1))
        mask += self.GetValueAt(pos + utils.Vec2(-1,  0))
        mask += self.GetValueAt(pos + utils.Vec2( 0,  0))
        mask += self.GetValueAt(pos + utils.Vec2(+1,  0))
        mask += self.GetValueAt(pos + utils.Vec2(-1, +1))
        mask += self.GetValueAt(pos + utils.Vec2( 0, +1))
        mask += self.GetValueAt(pos + utils.Vec2(+1, +1))
        index = int(mask, 2)
        result = self.algorithm[index]
        return True if result == '#' else False

    def GetValueAt(self, pos):
        if pos.X < self.x_min or pos.Y < self.y_min:
            # off the board
            return '1' if self.field else '0'
        if pos.X > self.x_max or pos.Y > self.y_max:
            # off the board
            return '1' if self.field else '0'
        return '1' if pos in self.points else '0'

    def GetExtents(self, ofs = 0):
        x_min = min([p.X for p in self.points]) - ofs
        x_max = max([p.X for p in self.points]) + ofs
        y_min = min([p.Y for p in self.points]) - ofs
        y_max = max([p.Y for p in self.points]) + ofs
        return x_min, x_max, y_min, y_max

    def PrintBoard(self):
        x_min, x_max, y_min, y_max = self.GetExtents(0)

        print(f"Lights = {len(self.points)}, [{x_min}, {y_min}], [{x_max}, {y_max}], Field={self.field}")
        return
        for yy in range(y_min, y_max+1):
            line = ''
            for xx in range(x_min, x_max+1):
                pos = utils.Vec2(xx, yy)
                pix = self.GetValueAt(pos)
                line += '#' if pix == '1' else '.'
            print(line)

if __name__ == "__main__":
    run()