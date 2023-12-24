import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

# Seems like the puzzles are taking on a new format this year, different input for the second
# part of the puzzle (at least for the sample data).
# Original data (for part 1) is:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# As a result, currentl need to run it with two different inputs.
# day1.py --debug --part1
# day1.py --debug --part2 --input sample_input_part2.txt


class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(1, "Weather Calibration", os.path.dirname(__file__))
        self.test_answers = [142, 281]
        self.answers = [52974, 53340]

    def parse_input(self):
        return

    def run_part1(self):
        # part1: find all the digits, pick the first and last
        pattern = r"(\d)"
        result = 0
        for line in self.input:
            result += self.get_digits(pattern, line)
        return result

    def run_part2(self):
        # part2: key here is the ?= which allows finding of overlapping string results.
        pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
        result = 0
        for line in self.input:
            result += self.get_digits(pattern, line)
        return result

    def get_digits(self, pattern, line):
        matches = re.findall(pattern, line)
        #print(matches)
        firstdigit = self.match_to_int(matches[0])
        lastdigit = self.match_to_int(matches[-1])
        result = firstdigit * 10 + lastdigit
        #print(f"{result} -> {matches[0]:6} {matches[-1]:6} {line}")
        return result
    
    def match_to_int(self, key):
        match_dict = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        return match_dict[key]



@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()