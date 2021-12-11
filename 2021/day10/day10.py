import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 10 *****")

    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    for line in input:
        line.Parse()

    # part 1:
    run_part1(input)

    # part 2:
    run_part2(input)

def run_part1(input):
    score = sum([line.GetScore() for line in input if line.corrupted is not None])
    print("part1: corrupted score = {0}".format(score))

def run_part2(input):
    scores = [line.GetScore() for line in input if line.autocomplete is not None]
    scores.sort()
    score = scores[len(scores)>>1] # number of scores will always be odd
    print("part2: autocomplete score = {0}".format(score))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [Puzzle(line.strip()) for line in f]
    f.close()
    return input

class Puzzle:
    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']
    part1 = [3, 57, 1197, 25137]
    part2 = [1, 2, 3, 4]

    def __init__(self, line):
        self.line = line
        self.corrupted = None
        self.autocomplete = None

    def Parse(self):
        # parse the single line of the puzzle input.
        # if corrupted; self.corrupted = score
        # if autocomplete; self.autocomplete = remaining characters
        stack = []
        for ch in self.line:
            if ch in Puzzle.openers:
                stack.append(ch)
            elif ch in Puzzle.closers:
                last = stack.pop() # pop last opener off the list
                expected = Puzzle.closers[Puzzle.openers.index(last)]
                if ch == expected:
                    continue
                #print("expected: {0} found {1}".format(expected, ch))
                self.corrupted = Puzzle.part1[Puzzle.closers.index(ch)]
                return # we're done

        if len(stack) > 0: # not corrupted, needs autocomplete
            self.autocomplete = stack

    def GetScore(self):
        # GetScore for either case; makes the "part1/part2" function up above look similar
        if self.corrupted is not None:
            return self.corrupted

        score = 0
        for ch in reversed(self.autocomplete):
            score *= 5
            score += Puzzle.part2[Puzzle.openers.index(ch)]
        #print("autocomplete = {0} ({1})".format(self.autocomplete, score))

        return score

if __name__ == "__main__":
    run()