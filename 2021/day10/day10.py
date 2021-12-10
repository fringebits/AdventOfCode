import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 10 *****")

    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    # part 1:
    run_part1(input)

    # part 2:
    run_part2(input)

def run_part1(input):
    ""
    score = 0
    for line in input:
        score += line.Parse()
    print("part1: corrupted score = {0}".format(score))

def run_part2(map):
    ""
    #print("part2: basins = {0}".format(result))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [Puzzle(line.strip()) for line in f]
    f.close()
    return input

class Puzzle:
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']
    scores = [3, 57, 1197, 25137]

    def __init__(self, line):
        self.line = line

    def Parse(self):
        score = 0
        stack = []
        for ch in self.line:
            if ch in Puzzle.openers:
                stack.append(ch)
            elif ch in Puzzle.closers:
                last = stack.pop() # pop last opener off the list
                expected = Puzzle.closers[Puzzle.openers.index(last)]
                if ch == expected:
                    continue
                print("expected: {0} found {1}".format(expected, ch))
                score += Puzzle.scores[Puzzle.closers.index(ch)]
                break
        return score

if __name__ == "__main__":
    run()