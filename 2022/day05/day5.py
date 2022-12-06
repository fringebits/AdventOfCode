import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

class Move:
    def __init__(self, count, source, target):
        self.count = int(count)
        self.source = int(source)
        self.target = int(target)

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(5, "Supply Stacks", os.path.dirname(__file__))
        self.test_answers = ['CMZ', 'MCD']
        self.answers = ['GRTSWNJHH', 'QLFQDBBHM']

    def parse_input(self):
        re_move = re.compile('move (\d+) from (\d+) to (\d+)')
        self.stacks = ['', '', '', '', '', '', '', '', '', '']
        self.moves = []
        for line in self.input:
            match = re_move.match(line)
            if match is not None:
                self.moves.append(Move(match.group(1), match.group(2), match.group(3)))
            elif '[' in line:
                index = 1
                while len(line) > 1:
                    match = re.match('^\[([A-Z])\]', line)
                    if match is not None:
                        self.stacks[index] += match.group(1)
                    line = line[4:]
                    index += 1

    def execute_move_part1(self, move: Move):
        # move item from stack to stack, one at a time
        for ii in range(move.count):
            item = self.stacks[move.source][0]
            self.stacks[move.source] = self.stacks[move.source][1:]
            self.stacks[move.target] = item + self.stacks[move.target]

    def execute_move_part2(self, move: Move):
        # move item from stack to stack, multiple at a time
        item = self.stacks[move.source][0:move.count]
        self.stacks[move.source] = self.stacks[move.source][move.count:]
        self.stacks[move.target] = item + self.stacks[move.target]

    def dump_stacks(self):
        for ii in range(1,10):
            print(f"{ii}: {self.stacks[ii]}")

    def top_crates(self):
        # top crates
        tops = ''
        for ii in range(1,10):
            if len(self.stacks[ii]) > 0:
                tops += self.stacks[ii][0]
        return tops

    def run_part1(self):
        for move in self.moves:
            self.execute_move_part1(move)
        return self.top_crates()

    def run_part2(self):
        self.parse_input() # need to 'reparse' the input because part1 is destructive on 'stacks'
        for move in self.moves:
            self.execute_move_part2(move)
        return self.top_crates()

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()