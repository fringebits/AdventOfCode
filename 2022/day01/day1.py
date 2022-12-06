import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        self.elf = []
        super().__init__(1, "Calorie Counting", os.path.dirname(__file__))
        self.test_answers = [24000, 45000]
        self.answers = [74394, 212836]

    def parse_input(self):
        self.elf = [0]
        ii = 0
        for line in self.input:
            if len(line) == 0:
                self.elf.append(0)
                ii += 1
            else:
                self.elf[ii] += int(line) 

    def run_part1(self):
        # part1: run the puzzle 10x
        result = max(self.elf)
        return result

    def run_part2(self):
        # part2: run the puzzle 10x
        input = self.elf
        hit = max(input)
        result = hit
        input.remove(hit)
        hit = max(input)
        result += hit
        input.remove(hit)
        hit = max(input)
        result += hit 
        return result

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()