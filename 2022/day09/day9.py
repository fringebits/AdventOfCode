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

class Bridge(utils.Grid):
    def __init__(self, width, height):
        super().__init__(width, height, 0)
        self.start = utils.Vec2(width >> 1, height >> 1)
        self.head = self.start
        self.tail = self.head
        self.set(self.tail.Y, self.tail.X, 1) # mark starting tail position

    def move(self, step):
        # moves are *never* diagnol
        for ii in range(abs(step.X)):
            self.move_one(utils.Vec2(sign(step.X), 0))

        for ii in range(abs(step.Y)):
            self.move_one(utils.Vec2(0, sign(step.Y)))
        #self.print_board()

    def move_one(self, step, R=1):
        self.head += step
        assert self.contains(self.head), f'HEAD {self.head} is off the grid'

        delta = self.tail - self.head

        if abs(delta.X) <= R and abs(delta.Y) <= R:
            return

        if delta.Y == 0:
            self.tail += utils.Vec2(-sign(delta.X) * (abs(delta.X) - R), 0)
        elif delta.X == 0:
            self.tail += utils.Vec2(0, -sign(delta.Y) * (abs(delta.Y) - R))
        else:
            self.tail += utils.Vec2(-sign(delta.X), -sign(delta.Y))

        assert self.contains(self.tail), f'TAIL {self.tail} is off the grid'
        self.set(self.tail.Y, self.tail.X, 1)
 
    def is_valid(self):
        delta = self.tail - self.head
        return abs(delta.X) > 1 or abs(delta.Y) > 1

    def print_board(self):
        for rr in range(self.height-1, -1, -1):
            line = ''
            for cc in range(self.width):
                pos = utils.Vec2(cc, rr)
                if pos == self.head:
                    pix = 'H'
                elif pos == self.tail:
                    pix = 'T'
                elif pos == self.start:
                    pix = 's'
                else:
                    pix = self.GetValueAt(pos).__str__()
                line += pix
            print(line)
        print('\n====\n')

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        self.moves = []
        super().__init__(9, "Rope Bridge", os.path.dirname(__file__))
        self.test_answers = [13, None]
        # self.answers = [1647, 392080]
        self.Bridge = Bridge(1024, 1024)

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
        #self.Bridge.reset()
        for move in self.moves:
            self.Bridge.move(move)
        score = sum([x for x in self.Bridge.data if isinstance(x, int)])
        return score



@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()