import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

import re

@utils.timer
def run():
    print("\n***** Day 13 *****")

    #input = load_input('test_input.txt')
    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    puzzle = Puzzle(input)

    # part 1:
    run_part1(puzzle)

    # part 2:
    run_part2(puzzle)

def run_part1(puzzle):
    # part1
    count = puzzle.ExecuteFolds(range(1))
    print("part1: visible points = {0}".format(count))
    assert count == 755, f"Unexpected count={count}, expected {755}, should read BLKJRBAG!"

def run_part2(puzzle):
    # part2: execute remaining folds, read the letters
    count = puzzle.ExecuteFolds(range(1, len(puzzle.folds)))
    puzzle.PrintBoard()
    assert count == 101, f"Unexpected count={count}, expected {101}, should read BLKJRBAG!"
    print("part2: visible points = {0}".format(count))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input

class Puzzle:
    def __init__(self, input):

        self.dim = utils.Vec2(0,0)
        self.points = set()
        self.folds = []

        point_ex = re.compile("(\d+),(\d+)")
        fold_ex = re.compile("fold along ([x|y])=(\d+)")

        # parse the input to create the puzzle
        for line in input:
            match = point_ex.match(line)
            if match is not None:
                x = int(match.group(1))
                y = int(match.group(2))
                self.points.add(utils.Vec2(x, y))
                continue
            match = fold_ex.match(line)
            if match is not None:
                self.folds.append((match.group(1), int(match.group(2))))
                continue
            if len(line) > 0:
                print(f"Unrecognized input line [{line}]")
        
        x = max([p.X for p in self.points]) + 1
        y = max([p.Y for p in self.points]) + 1
        self.dim = utils.Vec2(x, y)

    def ExecuteFolds(self, fold_range):
        for ii in fold_range:
            axis = self.folds[ii][0]
            value = self.folds[ii][1]
            self.ExecuteFoldInternal(axis, value)
            #self.PrintBoard()

        return len(self.points)

    def ExecuteFoldInternal(self, axis, value):
        #print(f"Fold along {axis}={value}")
        if axis == 'y':
            movers = [p for p in self.points if p.Y > value] # these points are "below the fold"
            for p in movers:
                self.points.discard(p)
                self.points.add(utils.Vec2(p.X, 2 * value - p.Y))
            self.dim = utils.Vec2(self.dim.X, value)
        elif axis == 'x':
            movers = [p for p in self.points if p.X > value] # these points are "below the fold"
            for p in movers:
                self.points.discard(p)
                self.points.add(utils.Vec2(2 * value - p.X, p.Y))
            self.dim = utils.Vec2(value, self.dim.Y)

    def PrintBoard(self):
        for yy in range(0, self.dim.Y):
            line = ""
            for xx in range(0, self.dim.X):
                if utils.Vec2(xx,yy) in self.points:
                    line = line + '*'
                else:
                    line = line + ' '
            print(line)
        #print(f"visible dots = {len(self.points)}")

if __name__ == "__main__":
    run()