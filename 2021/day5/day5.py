
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

@utils.timer
def run():
    print("\n***** Day 4 *****")

    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    # part 1:
    run_part1(input)

    # part 2:
    run_part2(input)

def run_part1(input):
    board = Board(input, False)
    overlaps = board.CountOverlaps()
    print("Part1: overlaps = {0}".format(overlaps))
    
def run_part2(input):
    board = Board(input, True)
    overlaps = board.CountOverlaps()
    print("Part2: overlaps = {0}".format(overlaps))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    wires = [Wire(x) for x in input]
    # for wire in wires:
    #     print(wire)
    return wires

class Wire:
    def __init__(self, input):
        match = re.compile("(\d+),(\d+) -> (\d+),(\d+)").match(input)
        self.a = utils.Vec2(int(match.group(1)), int(match.group(2)))
        self.b = utils.Vec2(int(match.group(3)), int(match.group(4)))

    def __str__(self):
        return "{0},{1} -> {2},{3}".format(self.a.X, self.a.Y, self.b.X, self.b.Y)

    def Slope(self):
        dy = self.a.Y - self.b.Y
        dx = self.a.X - self.b.X
        if dx == 0:
            return None
        return int(dy / dx)

class Board:
    def __init__(self, wires, allowDiagonal):
        x = max([max(wire.a.X, wire.b.X) for wire in wires]) + 1
        y = max([max(wire.a.Y, wire.b.Y) for wire in wires]) + 1
        self.dim = utils.Vec2(x, y)
        self.data = [0] * (x * y)
        for wire in wires:
            self.AddWire(wire, allowDiagonal)

    def AddWire(self, wire, allowDiagonal):
        slope = wire.Slope()

        step = utils.Vec2(0, 0)
        if slope == None:
            # vertical wire
            step.Y = -1 if wire.a.Y > wire.b.Y else 1
        elif slope == 0:
            # horizontal wire
            step.X = -1 if wire.a.X > wire.b.X else 1
        elif allowDiagonal and (slope == 1 or slope == -1):
            # diaganol wire
            step.X = -1 if wire.a.X > wire.b.X else 1
            step.Y = -1 if wire.a.Y > wire.b.Y else 1
        else:
            return

        #print("Adding wire: {0}".format(wire))
        pos = wire.a
        while True:
            self.Increment(pos.X, pos.Y)
            if pos == wire.b:
                break
            pos += step
        #self.PrintBoard()

    def Increment(self, x, y):
        index = x + y * self.dim.X
        self.data[index] += 1

    def CountOverlaps(self):
        overlaps = [d for d in self.data if d >= 2]
        return len(overlaps)

    def PrintBoard(self):
        for ii in range(0, self.dim.Y):
            a = ii * self.dim.X
            b = (ii+1) * self.dim.X
            row = ["{0} ".format('.' if v==0 else v) for v in self.data[a:b]]
            print("".join(row))
        print("---")

if __name__ == "__main__":
    run()