import os
import sys
import math

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

## https://adventofcode.com/2022/day/10

## Test Solution: (part2)
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....

class Instruction:
    def __init__(self, input:str):
        # there are only two instructions, default is noop
        self.cycles = 1
        self.value = 0
        if input.startswith('addx'):
            self.value = int(input.split(' ')[1])  # is this cheaper than a compiled regex?
            self.cycles = 2

class CRT(utils.Grid):
    def __init__(self, width, height):
        super().__init__(width, height, '.')
        self.cycle = 0 # pos = (self.cycle % self.width), int(self.cycle/self.width)
        self.X = 1 # sprite pos

    def execute(self, ii:Instruction):
        if self.cycle >= 240:
            return None

        if ii.cycles == 1: # noop
            self.tick()
        elif ii.cycles == 2: # addx
            self.tick()
            self.tick()
            self.X += ii.value

    def tick(self):
        pix = utils.Vec2(self.cycle % self.width, int(self.cycle / self.width))
        if pix.X >= self.X-1 and pix.X <= self.X+1:
            self.SetValueAt(pix, '#')
        self.cycle += 1

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        self.instructions = []
        super().__init__(10, "Cathode-Ray Tube", os.path.dirname(__file__))
        self.test_answers = [13140, None]
        self.answers = [11220, '\n###..####.###...##....##.####.#....#..#.\n' + '#..#....#.#..#.#..#....#.#....#....#.#..\n' + '###....#..#..#.#..#....#.###..#....##...\n' +  '#..#..#...###..####....#.#....#....#.#..\n' + '#..#.#....#....#..#.#..#.#....#....#.#..\n' + '###..####.#....#..#..##..####.####.#..#.\n']
        # letters should be:  BZPAJELK
        
    def parse_input(self): 
        self.instructions = [Instruction(x) for x in self.input]

    def run_part1(self):
        cycles = [x for x in range(20, 220 + 1, 40)]
        signals = []
        X = 1 # starting value
        cycle = 0
        for ii in self.instructions:
            new_cycle = cycle + ii.cycles
            new_X = X + ii.value
            if (new_cycle >= cycles[0]):
                signals.append(cycles[0] * X)
                cycles.pop(0)
                if (len(cycles) == 0):
                    break
            cycle = new_cycle
            X = new_X
        return sum(signals)

    def run_part2(self):
        crt = CRT(40, 6)
        for ii in self.instructions:
            crt.execute(ii)
        return '\n'+crt.__str__()

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()