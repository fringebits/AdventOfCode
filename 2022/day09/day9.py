import os
import sys
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

## https://adventofcode.com/2022/day/9

def sign(num):
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0

class Bridge():
    def __init__(self, num_knots):
        self.start = utils.Vec2(0, 0)
        self.knots = [self.start for x in range(num_knots + 1)]
        self.visited = { self.start }

    def move(self, step):
        # moves are *never* diagnol
        for ii in range(abs(step.X)):
            self.knots[0] += utils.Vec2(sign(step.X), 0)
            self.resolve_knots()

        for ii in range(abs(step.Y)):
            self.knots[0] += utils.Vec2(0, sign(step.Y))
            self.resolve_knots()

    def resolve_knots(self):
        for kk in range(1,len(self.knots)):
            self.knots[kk] = self.resolve_knot(self.knots[kk-1], self.knots[kk])
            if kk == len(self.knots)-1:
                self.visited.add(self.knots[kk])

    def resolve_knot(self, head, knot):
        delta = knot - head

        if abs(delta.X) <= 1 and abs(delta.Y) <= 1:
            return knot

        if delta.Y == 0:
            knot += utils.Vec2(-sign(delta.X) * (abs(delta.X) - 1), 0)
        elif delta.X == 0:
            knot += utils.Vec2(0, -sign(delta.Y) * (abs(delta.Y) - 1))
        else:
            knot += utils.Vec2(-sign(delta.X), -sign(delta.Y))

        return knot
 
    # def print_board(self):
    #     for rr in range(self.height-1, -1, -1):
    #         line = ''
    #         for cc in range(self.width):
    #             pos = utils.Vec2(cc, rr)
    #             if pos == self.head:
    #                 pix = 'H'
    #             elif pos == self.tail:
    #                 pix = 'T'
    #             elif pos == self.start:
    #                 pix = 's'
    #             else:
    #                 pix = self.GetValueAt(pos).__str__()
    #             line += pix
    #         print(line)
    #     print('\n====\n')

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        self.moves = []
        super().__init__(9, "Rope Bridge", os.path.dirname(__file__))
        self.test_answers = [88, 36]
        self.answers = [6464, 2604]

    def parse_input(self):        
        for line in self.input:
            match = re.match('(\S) (\d+)', line)
            dir = match.group(1)
            val = int(match.group(2))
            #print(line)
            if dir == 'U':
                move = utils.Vec2(0, +val)
            elif dir == 'D':
                move = utils.Vec2(0, -val)
            elif dir == 'L':
                move = utils.Vec2(-val, 0)
            elif dir == 'R':
                move = utils.Vec2(+val, 0)
            else:
                assert False, f'Invalid move input'
            self.moves.append(move)

    def run_part1(self):
        bridge = Bridge(1) # 1 knot
        for move in self.moves:
            bridge.move(move)
        score = len(bridge.visited)
        return score

    def run_part2(self):
        bridge = Bridge(9) # 9 knots
        for move in self.moves:
            bridge.move(move)
        score = len(bridge.visited)
        return score

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()