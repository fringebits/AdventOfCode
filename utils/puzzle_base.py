import os
import argparse
from .timer import timer

class PuzzleBase:
    def __init__(self, day, description, data_path):
        self.data_path = data_path
        self.answers = [None, None]
        self.test_answers = [None, None]

        parser = argparse.ArgumentParser()
        parser.add_argument("--debug", help="Debug mode, forces use of windows", action="store_true")
        self.args = parser.parse_args()

        print(f"\n***** Day {day}: {description} *****")
        self.input = []
        if self.args.debug:
            self.load_input('sample_input.txt')
        else:
            self.load_input('input.txt')
        self.parse_input()

    def run(self):
        if self.args.debug:
            expected = self.test_answers
        else:
            expected = self.answers

        self.results = [None, None]

        self.results[0] = self.run_part1()
        if expected[0] is None or expected[0] == self.results[0]:
            print(f'part 1: {self.results[0]}')
        else:
            print(f'part 1: {self.results[0]} FAIL, expected {expected[0]}')
        
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