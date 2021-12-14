import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

from collections import Counter

import re

@utils.timer
def run():
    print("\n***** Day 14 *****")

    input = load_input('test_input.txt')
    #input = load_input('sample_input.txt')
    #input = load_input('input.txt')

    puzzle = Puzzle(input)

    # part 1:
    run_part1(puzzle)

    # part 2:
    #run_part2(puzzle)

def run_part1(puzzle):
    # part1: run the puzzle 10x
    result = puzzle.Run(10)
    common = Counter(result).most_common()
    score = common[0][1] - common[-1][1]
    #assert score == 3143
    print(f"part1: polymer len = {len(result)} score = {score}")
    #assert count == 755, f"Unexpected count={count}, expected {755}, should read BLKJRBAG!"

def run_part2(puzzle):
    # part2: execute remaining folds, read the letters
    result = puzzle.Run(40)
    common = Counter(result).most_common()
    score = common[0][1] - common[-1][1]
    print(f"part2: polymer len = {len(result)} score = {score}")

def load_input(filename):

    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input

class Puzzle:
    def __init__(self, input):

        self.rules = dict()

        self.template = input[0]
        input.pop(0)

        # parse the input to create the puzzle
        pair_ex = re.compile("(\w+) -> (\w+)")
        for line in input:
            match = pair_ex.match(line)
            if match is not None:
                a = match.group(1)
                b = match.group(2)
                self.rules[a] = a[0] + b
                continue
            assert len(line)==0, f"Unrecognized input line [{line}]"

    def Run(self, count):
        result = self.template
        for ii in range(count):
            result = self.RunOneStep(result)
            print(f"step {ii}: {result}")
        return result
    
    def RunOneStep(self, template):
        result = ""
        for ii in range(len(template)-1):
            key = template[ii:ii+2]
            result += self.rules[key]
        result += template[-1]
        return result

if __name__ == "__main__":
    run()