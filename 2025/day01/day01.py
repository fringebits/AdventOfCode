import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

# As a result, currentl need to run it with two different inputs.
# day1.py --debug --part1
# day1.py --debug --part2 --input sample_input_part2.txt

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(1, "Secret Entrance", os.path.dirname(__file__))
        self.test_answers = [3, 6]
        self.answers = [1123, 6695]

    def parse_input(self):
        return

    def run_part1(self):
        # part1: rotate the dial
        count = 0
        dial = 50        
        pattern = re.compile(r"([L|R])(\d+)")
        for line in self.input:
            ret = pattern.search(line)
            move = int(ret.group(2))
            if ret.group(1) == 'L':
                move = -move

            dial += move
            dial = dial % 100
            if dial == 0:
                count += 1
        return count

    def run_part2(self):
        # part1: rotate the dial
        count = 0
        dial = 50        
        pattern = re.compile(r"([L|R])(\d+)")
        for line in self.input:
            ret = pattern.search(line)
            move = int(ret.group(2))
            dir = 1

            if ret.group(1) == 'L':
                dir = -1                

            laps = int(move/100)
            move = (move - (laps * 100)) * dir
            delta = laps # one for each lap for sure
            start = dial

            if dir > 0:
                dial = dial - 100

            next = dial + move
            if (next * dial < 0):
                delta += 1
            dial = next % 100
            if dial == 0:
              delta += 1
            
            count = count + delta
            # if delta > 0:
            #     print(f"rot {line} dial={dial%100}, delta={delta}")
            # else:
            #     print(f"rot {line} dial={dial%100}")
            
        return count

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()