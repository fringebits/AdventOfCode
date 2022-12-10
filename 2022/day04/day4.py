import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(4, "Camp Cleanup", os.path.dirname(__file__))
        self.test_answers = [2, 4]
        self.answers = [453, 919]

    def parse_input(self):
        self.ranges = []
        for line in self.input:
            pairs = line.split(',')
            r = pairs[0].split('-')
            A = utils.Range(int(r[0]), int(r[1]))
            r = pairs[1].split('-')
            B = utils.Range(int(r[0]), int(r[1]))
            self.ranges.append([A, B])

    def run_part1(self):
        # compute full containment
        count = 0
        for r in self.ranges:
            if r[0].contains(r[1]) or r[1].contains(r[0]):
                count += 1
        return count

    def run_part2(self):
        # compute overlap
        count = 0
        for r in self.ranges:
            if r[0].overlaps(r[1]):
                count += 1
        return count

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()
