import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

from collections import Counter

import re

@utils.timer
def run():
    print("\n***** Day 1 *****")

    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    # part 1:
    run_part1(input)

    # part 2:
    run_part2(input)

def run_part1(input):
    # part1: run the puzzle 10x
    result = max(input)
    print(f"part1: elf calories = {result}")
    #assert count == 755, f"Unexpected count={count}, expected {755}, should read BLKJRBAG!"

def run_part2(input):
    # part2: run the puzzle 10x
    hit = max(input)
    result = hit
    input.remove(hit)
    hit = max(input)
    result += hit
    input.remove(hit)
    hit = max(input)
    result += hit 
    print(f"part1: elf calories = {result}")
    #assert count == 755, f"Unexpected count={count}, expected {755}, should read BLKJRBAG!"

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    elf = [0]
    ii = 0
    for line in [line.strip() for line in f]:
        if len(line) == 0:
            elf.append(0)
            ii += 1
        else:
            elf[ii] += int(line) 
    f.close()
    return elf

class Puzzle:
    def __init__(self, input):
        return

    def Run(self, count):
        return 0

if __name__ == "__main__":
    run()