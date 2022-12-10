import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(6, "Tuning Trouble", os.path.dirname(__file__))
        self.answers = [1140, None]
        self.test_answers = [5, 23]

    def test_marker(line, count):
        for ii in range(0, len(line)-count):
            marker = set(line[ii:ii+count])
            if len(marker) == count:
                #print(f"marker={marker}, ii={ii+count}")
                return ii+count

    def run_part1(self):
        return Puzzle.test_marker(self.input[0], 4)

    def run_part2(self):
        return Puzzle.test_marker(self.input[0], 14)

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()