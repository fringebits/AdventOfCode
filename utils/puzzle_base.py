import os
import os.path
import argparse
from .timer import timer

class PuzzleBase:
    def __init__(self, day, description, data_path):
        self.data_path = data_path
        self.answers = [None, None]
        self.test_answers = [95437, None]

        parser = argparse.ArgumentParser()
        parser.add_argument("--debug", help="Debug mode, forces use of windows", action="store_true")
        parser.add_argument("--part1", help="Run part1 only", action="store_true")
        parser.add_argument("--part2", help="Run part2 only", action="store_true")
        parser.add_argument("--input", help="Input file to use, other than default")
        self.args = parser.parse_args()

        # todo: need to allow a way to provide a different input for each part, specifically for debug
        # seems like it would make sense to move the "load_input" closer to execution of the puzzle part
        # and if the alternative input file exists, then we load it and re-parse the input

        print(f"\n***** Day {day}: {description} *****")
        self.input = []

        input_file = 'input.txt'
        if self.args.input is not None and os.path.isfile(self.args.input):
            input_file = self.args.input
        elif self.args.debug:
            input_file = 'sample_input.txt'

        self.load_input(input_file)
        self.parse_input()

    def run(self):
        if self.args.debug:
            expected = self.test_answers
        else:
            expected = self.answers

        self.results = [None, None]

        if not self.args.part2:
            self.results[0] = self.run_part1()
            if expected[0] is None or expected[0] == self.results[0]:
                print(f'part 1: {self.results[0]}')
            else:
                print(f'part 1: {self.results[0]} FAIL, expected {expected[0]}')

        if not self.args.part1:

            # if the _part2.txt sample input exists, we load and parse it here
            if self.args.debug and os.path.isfile('sample_input_part2.txt'):
                self.load_input('sample_input_part2.txt')
                self.parse_input()

            self.results[1] = self.run_part2()
            if expected[1] is None or expected[1] == self.results[1]:
                print(f'part 2: {self.results[1]}')
            else:
                print(f'part 2: {self.results[1]} FAIL, expected {expected[1]}')

    def run_part1(self):
        pass

    def run_part2(self):
        pass

    def parse_input(self):
        pass
        
    def load_input(self, filename):
        f = open(os.path.join(self.data_path, filename), 'r')
        self.input = [ line.rstrip() for line in f]
        f.close()